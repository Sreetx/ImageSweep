pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'imagesweep'

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'imagesweep.in',
           output: 'imagesweep',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir'),
     install_mode: 'r-xr-xr-x'
)

imagesweep_sources = [
    '__init__.py',
    'main.py'
]

install_data(imagesweep_sources, install_dir: moduledir)
