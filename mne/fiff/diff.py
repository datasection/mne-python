# Author: Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#
# License: BSD Style.

import numpy as np

import logging
logger = logging.getLogger('mne')


def is_equal(first, second, verbose=True):
    """ Says if 2 python structures are the same. Designed to
    handle dict, list, np.ndarray etc.
    """
    all_equal = True
    # Check all keys in first dict
    if type(first) != type(second):
        all_equal = False
    if isinstance(first, dict):
        for key in first.keys():
            if (not key in second):
                if verbose:
                    logger.info("Missing key %s in %s" % (key, second))
                all_equal = False
            else:
                if not is_equal(first[key], second[key]):
                    all_equal = False
    elif isinstance(first, np.ndarray):
        if not np.allclose(first, second):
            all_equal = False
    elif isinstance(first, list):
        for a, b in zip(first, second):
            if not is_equal(a, b):
                if verbose:
                    logger.info('%s and\n%s are different' % (a, b))
                all_equal = False
    else:
        if first != second:
            if verbose:
                logger.info('%s and\n%s are different' % (first, second))
            all_equal = False
    return all_equal
