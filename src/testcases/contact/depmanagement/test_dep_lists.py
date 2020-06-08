#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apis.contact.departmet.depmanagment import DeptManagement
from utils.readyaml import *
import pytest

@pytest.mark.DepLists
class TestDepLists:

    @pytest.mark.smoke
    @pytest.mark.Success
    def test_dep_lists_no_id(self):
        dept_management = DeptManagement()
        dept_management.get_dep_lists()
        dep_lists = dept_management.get_response()
        assert len(dep_lists.get('department')) > 0

    # def test_dep_lists_id_null(self):
    #     dept_management = DeptManagement()
    #     id = (Read_File_Yaml('../testdata/delete_dep.yaml')).get('dep_id1').get("id")
    #     dept_management.get_dep_lists(id)
    #     dep_lists = dept_management.get_response()
    #     assert dep_lists.get('errcode') == 60004

    @pytest.mark.Success
    def test_dep_lists_id1(self):
        dept_management = DeptManagement()
        id = (Read_File_Yaml('../testdata/delete_dep.yaml')).get('dep_id2').get("id")
        dept_management.get_dep_lists(id)
        dep_lists = dept_management.get_response()
        assert len(dep_lists.get('department')) == 2

    @pytest.mark.Success
    def test_dep_lists_id2(self):
        dept_management = DeptManagement()
        id = (Read_File_Yaml('../testdata/delete_dep.yaml')).get('dep_id3').get("id")
        dept_management.get_dep_lists(id)
        dep_lists = dept_management.get_response()
        assert len(dep_lists.get('department')) == 1

    @pytest.mark.Fail
    def test_dep_lists_id_not_exist(self):
        dept_management = DeptManagement()
        id = (Read_File_Yaml('../testdata/delete_dep.yaml')).get('dep_id4').get("id")
        dept_management.get_dep_lists(id)
        dep_lists = dept_management.get_response()
        assert len(dep_lists.get('department')) == 0