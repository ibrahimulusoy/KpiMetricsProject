from setuptools import setup, find_packages

setup(name='kpimetrics',
      version='0.1',
      url='https://github.com/ibrahimulusoy/KpiMetricsProject.git',
      #license='MIT',
      author='Harmony Public Schools',
      author_email='eatakahraman@harmonytx.org',
      description='Kpi Metrics project',
      packages=find_packages(),#exclude=['tests']
      #long_description=open('README.md').read(),
      zip_safe=False)