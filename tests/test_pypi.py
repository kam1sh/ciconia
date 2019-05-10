import subprocess
from pathlib import Path
import base64

import pytest
from packaging.utils import canonicalize_version
from django.test import Client
from django.core.files.uploadedfile import File

import ciconia
from ciconia.pypi import models


PACKAGES = dict(
    sdist=next(Path("dist").glob("*.whl")),
    bdist_wheel=next(Path("dist").glob("*.tar.gz")),
)

FORM = {
    "name": "ciconia",
    "version": "0.1.0",
    "filetype": None,
    "pyversion": "",
    "metadata_version": "2.1",
    "summary": "Ciconia test package",
    "home_page": "",
    "author": "Igor Ovsyannikov",
    "author_email": "kamish@outlook.com",
    "maintainer": "Igor Ovsyannikov",
    "maintainer_email": "kamish@outlook.com",
    "license": "MIT",
    "description": "",
    "keywords": "",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    "download_url": "",
    "comment": "",
    "sha256_digest": None,
    "requires_dist": ["flask (>=1.0,<2.0)", "docker (>=3.7,<4.0)"],
    "requires_python": ">=3.6,<4.0",
    ":action": "file_upload",
    "protocol_version": "1",
}


@pytest.yield_fixture(scope="function", params=PACKAGES)
def dist(request):
    pkg_type = request.param
    file_ = PACKAGES[pkg_type]
    form = FORM.copy()
    form["filetype"] = pkg_type
    form["sha256_digest"] = sha256sum(file_)
    with file_.open("rb") as f:
        form["file"] = f
        yield form


def sha256sum(pth: Path):
    return subprocess.check_output(
        ["sha256sum", pth.absolute()], encoding="utf-8"
    ).split()[0]


@pytest.mark.unit
def test_readers(dist):
    """Tests for package reading (wheel and tar.gz)"""
    file_ = dist.pop("file")
    pkg = models.PackageFile(pkg=file_, metadata=dist)
    origname = Path(file_.name).name
    assert pkg.filename == origname
    assert pkg.fileobj.name == origname
    # metadata accessing
    assert pkg.name == "ciconia"
    assert pkg.version == canonicalize_version(ciconia.__version__)
    assert isinstance(pkg.metadata["requires_dist"], list)


def test_upload(dist, client, db):
    form = dist
    dist = dist.pop("file")
    form["content"] = File(dist)
    auth = "Basic: {}".format(base64.b64encode(b"test@localhost:123").decode())
    assert client.post("/py/upload/", form) == 401
    dist.seek(0)
    response = client.post("/py/upload/", form, HTTP_AUTHORIZATION=auth)
    print(response.content)
    assert response == 200
