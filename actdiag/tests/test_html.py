# -*- coding: utf-8 -*-

import os
import re
from .utils import with_built_docstring

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

png_config = dict(
    extensions=['sphinxcontrib.actdiag'],
    master_doc='index',
)

svg_config = dict(
    extensions=['sphinxcontrib.actdiag'],
    master_doc='index',
    actdiag_html_image_format='SVG',
)


class TestSphinxcontribActdiagHTML(unittest.TestCase):
    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_build_png_image(self, app):
        """
        .. actdiag::

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><img .*? src=".*?.png" .*?/></div>')

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_width_option_on_png(self, app):
        """
        .. actdiag::
           :width: 128

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="140.0" src="\\1" width="128.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_height_option_on_png(self, app):
        """
        .. actdiag::
           :height: 140

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="140.0" src="\\1" width="128.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_width_option_and_height_option_on_png(self, app):
        """
        .. actdiag::
           :width: 100
           :height: 200

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="200.0" src="\\1" width="100.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_scale_option_on_png(self, app):
        """
        .. actdiag::
           :scale: 25%

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="70.0" src="\\1" width="64.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_width_option_and_scale_option_on_png(self, app):
        """
        .. actdiag::
           :width: 28
           :scale: 25%

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="7.65625" src="\\1" width="7.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_align_option_on_png(self, app):
        """
        .. actdiag::
           :align: center

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div align="center" class="align-center"><img .*? /></div>')

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_align_option_and_width_option_on_png(self, app):
        """
        .. actdiag::
           :align: center
           :width: 128

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div align="center" class="align-center">'
                                              '<a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="140.0" src="\\1" width="128.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_name_option_on_png(self, app):
        """
        .. actdiag::
           :name: target

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><img .*? id="target" src=".*?" .*? /></div>')

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_name_option_and_width_option_on_png(self, app):
        """
        .. actdiag::
           :name: target
           :width: 128

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<img height="140.0" id="target" src="\\1" width="128.0" /></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_href_and_scale_option_on_png(self, app):
        """
        .. actdiag::
           :scale: 50%

           A -> B;
           A [href = 'http://blockdiag.com/'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><a class="reference internal image-reference" href="(.*?.png)">'
                                              '<map name="(map_\d+)">'
                                              '<area shape="rect" coords="32.0,60.0,96.0,80.0" '
                                              'href="http://blockdiag.com/"></map>'
                                              '<img .*? src="\\1" usemap="#\\2" .*?/></a></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_reftarget_in_href_on_png1(self, app):
        """
        .. _target:

        heading2
        ---------

        .. actdiag::

           A -> B;
           A [href = ':ref:`target`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><map name="(map_\d+)">'
                                              '<area shape="rect" coords="64.0,120.0,192.0,160.0" href="#target"></map>'
                                              '<img .*? src=".*?.png" usemap="#\\1" .*?/></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_reftarget_in_href_on_png2(self, app):
        """
        .. _hello world:

        heading2
        ---------

        .. actdiag::

           A -> B;
           A [href = ':ref:`hello world`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><map name="(map_\d+)">'
                                              '<area shape="rect" coords="64.0,120.0,192.0,160.0" href="#hello-world">'
                                              '</map><img .*? src=".*?.png" usemap="#\\1" .*?/></div>'))

    @with_built_docstring(buildername='html', confoverrides=png_config)
    def test_missing_reftarget_in_href_on_png(self, app):
        """
        .. actdiag::

           A -> B;
           A [href = ':ref:`unknown_target`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, ('<div><img .*? src=".*?.png" .*?/></div>'))
            self.assertIn('undefined label: unknown_target',
                          app.builder.warn.call_args_list[0][0][0])

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_build_svg_image(self, app):
        """
        .. actdiag::

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_width_option_on_svg(self, app):
        """
        .. actdiag::
           :width: 128

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg height="140.0" viewBox="0 0 256 280" width="128.0" .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_height_option_on_svg(self, app):
        """
        .. actdiag::
           :height: 140

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg height="140.0" viewBox="0 0 256 280" width="128.0" .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_width_option_and_height_option_on_svg(self, app):
        """
        .. actdiag::
           :width: 100
           :height: 200

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg height="200.0" viewBox="0 0 256 280" width="100.0" .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_scale_option_on_svg(self, app):
        """
        .. actdiag::
           :scale: 25%

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg height="70.0" viewBox="0 0 256 280" width="64.0" .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_width_option_and_scale_option_on_svg(self, app):
        """
        .. actdiag::
           :width: 28
           :scale: 25%

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><svg height="7.65625" viewBox="0 0 256 280" width="7.0" .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_align_option_on_svg(self, app):
        """
        .. actdiag::
           :align: center

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div align="center" class="align-center"><svg .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_name_option_on_svg(self, app):
        """
        .. actdiag::
           :name: target

           A -> B;
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<div><span id="target"></span><svg .*?>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_reftarget_in_href_on_svg1(self, app):
        """
        .. _target:

        heading2
        ---------

        .. actdiag::

           A -> B;
           A [href = ':ref:`target`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<a xlink:href="#target">\\n\\s*<rect .*?>\\n\\s*</a>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_reftarget_in_href_on_svg2(self, app):
        """
        .. _hello world:

        heading2
        ---------

        .. actdiag::

           A -> B;
           A [href = ':ref:`hello world`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            self.assertRegexpMatches(source, '<a xlink:href="#hello-world">\\n\\s*<rect .*?>\\n\\s*</a>')

    @with_built_docstring(buildername='html', confoverrides=svg_config)
    def test_missing_reftarget_in_href_on_svg(self, app):
        """
        .. actdiag::

           A -> B;
           A [href = ':ref:`unknown_target`'];
        """
        filename = os.path.join(app.outdir, 'index.html')
        with open(filename) as fd:
            source = fd.read()
            if sys.version_info < (3, 0):
                self.assertNotRegexpMatches(source, '<a xlink:href="#hello-world">\\n\\s*<rect .*?>\\n\\s*</a>')
            else:
                self.assertNotRegex(source, '<a xlink:href="#hello-world">\\n\\s*<rect .*?>\\n\\s*</a>')
            self.assertIn('undefined label: unknown_target',
                          app.builder.warn.call_args_list[0][0][0])
