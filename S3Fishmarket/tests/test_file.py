import unittest.mock as mock
import pytest
import S3Fishmarket.app.code as code


# Test to see if the number of a given species is correct


def test_check_length_of_file():
    assert len(code.combine_file) == 477


# def test_check_sum_of_length1():
#     assert code.calculate_avg_length1_for_given_species('Bream') == 1224.7171859399998
#
#
# def test_check_sum_of_length2():
#     assert code.calculate_length2_for_given_species('Bream') == 1345.7502271100002
#
#
# def test_check_sum_of_length3():
#     assert code.calculate_length3_for_given_species('Bream') == 1489.40278261
#
#
# def test_number_of_given_species():
#     assert code.calculate_number_of_species('Bream') == 35
