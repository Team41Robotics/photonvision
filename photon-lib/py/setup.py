from setuptools import setup, find_packages
import subprocess, re

gitDescribeResult = (
    subprocess.check_output(["git", "describe", "--tags", "--match=v*", "--always"])
    .decode("utf-8")
    .strip()
)

m = re.search(
    r"(v[0-9]{4}\.[0-9]{1}\.[0-9]{1})-?((?:beta)?(?:alpha)?)-?([0-9\.]*)",
    gitDescribeResult,
)

# Extract the first portion of the git describe result
# which should be PEP440 compliant
if m:
    versionString = m.group(0)
    prefix = m.group(1)
    maturity = m.group(2)
    suffix = m.group(3).replace(".", "")
    versionString = f"{prefix}.{maturity}.{suffix}"


else:
    print("Warning, no valid version found")
    versionString = gitDescribeResult

print(f"Building version {versionString}")

# Put the version info into a python file for runtime access
with open("photonlibpy/version.py", "w", encoding="utf-8") as fp:
    fp.write(f'PHOTONLIB_VERSION="{versionString}"\n')
    fp.write(f'PHOTONVISION_VERSION="{gitDescribeResult}"\n')


descriptionStr = f"""
Pure-python implementation of PhotonLib for interfacing with PhotonVision on coprocessors.
Implemented with PhotonVision version {gitDescribeResult} .
"""

setup(
    name="photonlibpy",
    packages=find_packages(),
    version=versionString,
    install_requires=[
        "wpilib<2025,>=2024.0.0b2",
        "robotpy-wpimath<2025,>=2024.0.0b2",
        "pyntcore<2025,>=2024.0.0b2",
    ],
    description=descriptionStr,
    url="https://photonvision.org",
    author="Photonvision Development Team",
    long_description="A Pure-python implementation of PhotonLib",
    long_description_content_type="text/markdown",
)
