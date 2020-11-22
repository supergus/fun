import setuptools

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    # Use VCS instead of MANIFEST to control included files & folders
    # Works for git and hg
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    include_package_data=True,  # Needed if using old MANIFEST.in?

    # Mandatory fields
    name='liveline_fun',
    # version='0.0.1.dev1',       # Does this overwrite version from VCS?
    packages=setuptools.find_packages(),    # Builds & wheels are limited to pkgs specified here

    # Optional fields
    # scripts=['bin/'],    # Rely on VCS?
    license='LICENSE',
    author='Christopher Couch',
    author_email='christopher.couch@gmail.com',
    description='Toolkit for various fun and useful tasks',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/cooper-standard/ll_fun',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3.7',
        'License :: None - Strictly proprietary and protected by copyright',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: GPU :: NVIDIA CUDA :: 10.1',
        'Natural Language :: English',
    ],

    keywords='liveline fun utilities',

    python_requires='>=3.7',
    # install_requires=['numpy', 'pandas', 'matplotlib', 'scikit_learn', 'statsmodels', 'scipy',
    #                   'pytz', 'pycryptodome', 'psycopg2', 'tqdm', 'xlrd', 'XlsxWriter',
    #                   'pywavelets', 'mpi4py', 'tensorflow', 'pydot'],
    project_urls={
        'Company': 'https://www.liveline.tech',
        'Source': 'https://github.com/cooper-standard/ll_fun',
    },
)
