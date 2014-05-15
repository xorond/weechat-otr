# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-public-methods

from __future__ import unicode_literals

from weechat_otr_test.weechat_otr_test_case import WeechatOtrTestCase

import weechat_otr
import weechat_otr_test.raising_account

class ContextMessageInCbTestCase(WeechatOtrTestCase):

    def test_action_encrypted(self):
        account = \
            weechat_otr_test.raising_account.RaisingAccount('nick@server')
        weechat_otr.ACCOUNTS['nick@server'] = account
        context = account.getContext('nick@server')
        context.unencrypted = ['\x01ACTION lols\x01']

        result = weechat_otr.message_in_cb(
            None, None, 'server', ':nick!user@host PRIVMSG friend :test')

        self.assertEqual(result,
            ':nick!user@host PRIVMSG friend :Unencrypted message received: '
            '/me lols')
