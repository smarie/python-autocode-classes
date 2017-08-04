from py.xml import html
import pytest
from setuptools_scm import version_from_scm


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """ adds the description field in the report, so that it may be used by the other two functions """
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """ Inserts the header for a 'description' column """
    cells[1] = html.th('Test File')
    cells.insert(2, html.th('Test'))
    cells.insert(3, html.th('Description'))
    # cells.insert(0, html.th('Time', class_='sortable time', col='time'))
    # cells.pop()  keep it : we will link to codecov here


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    """ Inserts the contents for the 'description' column : the docstring of the test function """
    node_bits = report.nodeid.split('::')
    cells[1] = html.th(node_bits[0])
    cells.insert(2, html.td('::'.join(node_bits[1:]) if len(node_bits) > 1 else ''))
    cells.insert(3, html.td(report.description))
    # cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    # cells.pop()

    # use setuptools_scm to get git hash and build the codecov URL to go and see the source of the test
    parsed_version = version_from_scm('.')
    if parsed_version is not None:
        hsh = parsed_version.node + ('' if not parsed_version.dirty else '-dirty')
        cells[-1] = html.td(html.a('source', href='https://codecov.io/gh/smarie/python-autoclass/src/' + hsh + '/'
                                                  + node_bits[0]))
    else:
        cells[-1] = html.td('could not parse git version')