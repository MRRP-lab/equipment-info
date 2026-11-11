from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ur_moveit_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            [os.path.join('resource/' + package_name)]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'srdf'), glob('srdf/ur.srdf*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alex Nilles',
    maintainer_email='nillesa2@wwu.edu',
    description='Minimal working example of Moveit Python API for UR',
    license='freeware',
    entry_points={
        'console_scripts': [
            'move_arm = ur_moveit_py.move_arm:main'],
    },
)
