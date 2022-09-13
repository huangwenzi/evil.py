import setuptools
import evilpy

setuptools.setup(
    name="evilpy",#这里是库名
    version="1.0.2",#版本
    packages = setuptools.find_packages(),
    author="hw",#开发人员
    author_email="811417477@qq.com",#开发人员邮箱
    description="",#一句话简介
    maintainer='hw',#维护者
    maintainer_email='811417477@qq.com',#维护者邮箱
    install_requires=[''],#依赖包
    long_description=open('README.md', encoding='utf-8').read(),#读取方法介绍文件
    classifiers=[
        "Programming Language :: Python",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],#编写时的应用
 
    python_requires='>=3.4',#Python的版本
    # package_dir={'': 'evilpy'}#需要上传的文件夹
) 
