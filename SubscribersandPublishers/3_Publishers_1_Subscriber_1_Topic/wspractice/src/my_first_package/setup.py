from setuptools import setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='My first ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = my_first_package.publisher_node:main',
            'subscriber_node = my_first_package.subscriber_node:main',
            'publisher_node_two = my_first_package.publisher_node_two:main',
            'publisher_node_three = my_first_package.publisher_node_three:main',
            
        ],
    },
)
