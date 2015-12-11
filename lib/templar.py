#!/usr/bin/env python

import sys, os
from jinja2 import FileSystemLoader, Environment, Template

class TemplarException(Exception): pass

class Templar(object):
  def __init__(self):
    """Constructor to specify the search path"""
    self.values = None
    self.source = None
    self.templateEnv = None

  def __set_template_env__(self):
    """Set the template Env so that it could
       find the templates"""
    __templateLoader__ = FileSystemLoader(searchpath=self.source)
    self.templateEnv = Environment(loader=__templateLoader__)

  def __render__(self, templateObject):
    return templateObject.render(self.values, trim_blocks=True, lstrip_blocks=True)

  def __dump__(self, templateObject, destPath):
    templateObject.stream(self.values, trim_blocks=True, lstrip_blocks=True).dump(destPath)

  def render_string(self, string):
    """Renders the string template and return a string"""
    __template__ = Template(string)
    return self.__render__(__template__)

  def dump_string(self, string, destPath):
    """Renders the string and dump it in the file"""
    __template__ = Template(string)
    self.__dump__(__template__, destPath)

  def render_template(self, filename):
    """Renders the template and return a string"""
    if self.templateEnv:
      __template__ = self.templateEnv.get_template(filename)
      return self.__render__(__template__)
    else:
      raise TemplarException("Source Directory not found, please set_sourceDirectory first")

  def dump_template(self, filename, destPath):
    """Render the template and dump in the file"""
    if self.templateEnv:
      __template__ = self.templateEnv.get_template(filename)
      self.__dump__(__template__, destPath)
    else:
      raise TemplarException("Source Directory not found, please set_sourceDirectory first")

  def set_sourceDirectory(self, srcPath):
    if os.path.isdir(srcPath):
      self.source = os.path.abspath( srcPath )
      self.__set_template_env__()
    else:
      raise TemplarException("Source Directory [%s] not found" %srcPath)

  def set_values(self, values={}):
    if isinstance(values, dict):
      self.values = values
    else:
      raise TemplarException("type<dict> exepected instead recieved %s" %type(values))
