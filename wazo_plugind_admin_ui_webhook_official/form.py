# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import (SubmitField,
                            StringField,
                            TextAreaField,
                            HiddenField,
                            FormField,
                            FieldList,
                            BooleanField,
                            SelectField)
from wtforms.validators import InputRequired, Length

from wazo_admin_ui.helpers.form import BaseForm


class UserForm(BaseForm):
    uuid = HiddenField()
    firstname = HiddenField()
    lastname = HiddenField()


class WebhookForm(BaseForm):
    name = StringField('Display name', [Length(max=100)])
    events = StringField('Event Name', [InputRequired(), Length(max=128)])
    services = SelectField('Services', choices=[])
    users = FieldList(FormField(UserForm))
    user = SelectField('User', choices=[])

class WebhookFormHTTP(WebhookForm):
    url = StringField('Target', [InputRequired(), Length(max=512)])
    method = SelectField('Method', choices=[('post', 'POST'), ('get', 'GET'), ('put', 'PUT'), ('delete', 'DELETE'), ('head', 'HEAD')])
    content_type = StringField('Content Type', [Length(max=100)], default='application/json')
    verify_certificate = BooleanField('Verify Certificate')
    body = TextAreaField('Body')
    submit = SubmitField('Submit')
