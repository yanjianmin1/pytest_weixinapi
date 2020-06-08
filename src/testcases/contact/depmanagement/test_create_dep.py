#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apis.contact.departmet.depmanagment import DeptManagement
import pytest

@pytest.mark.CreateDep
class TestCreatDep:

    @pytest.mark.smoke
    @pytest.mark.Success
    def test_create_new_dep(self):
        dept_management = DeptManagement()
        dept_management.create_dept_nameRandom("dep1")
        create_res = dept_management.get_response()
        assert create_res.get('errmsg') == 'created'

    @pytest.mark.Fail
    def test_create_exist_dep(self):
        dept_management = DeptManagement()
        dept_management.create_dept("dep2")
        create_res = dept_management.get_response()
        assert create_res.get('errcode') == 60008

    @pytest.mark.Fail
    def test_create_dep_name_null(self):
        dept_management = DeptManagement()
        dept_management.create_dept("dep3")
        create_res = dept_management.get_response()
        assert create_res.get('errcode') == 60001