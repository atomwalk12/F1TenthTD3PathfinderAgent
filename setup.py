from glob import glob
import os
from setuptools import setup

package_name = 'f1tenth_gym_agent'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob("launch/*.launch.py")),
        (os.path.join('share', package_name, 'worlds'), glob("worlds/*.world")),
        (os.path.join('share', package_name, 'urdf'), glob("urdf/*.urdf")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='razfv07@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'agent = f1tenth_gym_agent.rd3_agent:main',
        ],
    },
)
