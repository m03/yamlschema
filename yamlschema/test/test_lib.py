"""
Utility to import sample data and staff batch data, should import data
"""
import sys
import os

from jsonschema import ValidationError

from pytest import fixture

from mock import patch, Mock

from yamlschema.lib import validateconfig


@fixture
def options():
    opt = validateconfig.ValidateConfig()
    opt['configFile'] = aorta.fromaortaPackage('test/test_cli/test_config.yml')
    opt['schema'] = False


@fixture
def configGood():
    return aorta.fromaortaPackage('test/test_cli/test_config.schema.yml')
    

@fixture
def configBad():
    return aorta.fromaortaPackage('test/test_cli/test_config_bad.yml')


def test_postOptionsOk(self):
    """
    Does a good config pass?
    """
    pCONFIG_SCHEMA_YML = patch.object(aorta, 'CONFIG_SCHEMA_YML', self.configSchema)
    pOut = patch.object(sys, 'stdout', autospec=True)
    pErr = patch.object(sys, 'stderr', autospec=True)
    with pCONFIG_SCHEMA_YML, pOut, pErr:
        x = self.opt.postOptions()
        self.assertEqual(True, x)

def test_postOptionsBad(self):
    """
    Does a bad config fail?
    """
    pCONFIG_SCHEMA_YML = patch.object(aorta, 'CONFIG_SCHEMA_YML', self.configSchema)
    pOut = patch.object(sys, 'stdout', autospec=True)
    pErr = patch.object(sys, 'stderr', autospec=True)
    self.opt['configFile'] = self.configBad

    with pCONFIG_SCHEMA_YML, pOut, pErr:
        self.assertRaises(ValidationError, self.opt.postOptions)

def test_postOptionsSchema(self):
    """
    Can we display a normalized yaml output?
    """
    pOut = patch.object(sys, 'stdout', autospec=True)
    pErr = patch.object(sys, 'stderr', autospec=True)
    self.opt['schema'] = True
    self.opt['configFile'] = self.configSchema

    with pOut, pErr:
        x = self.opt.postOptions()
        self.assertRegexpMatches(x, r'debug: {type: boolean}')

def test_parseArgs(self):
    """
    Do we check permissions on files and report those errors?
    """
    with patch.object(os, 'access', Mock(return_value=False)):
        self.assertRaises(OSError, self.opt.parseArgs, 'adafds')
    with patch.object(os, 'access', Mock(return_value=True)):
        self.opt.parseArgs('cheeses')
        self.assertEqual(self.opt['configFile'], 'cheeses')

