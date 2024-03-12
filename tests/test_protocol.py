from nicostick.protocol import Stick3Protocol


def test_scene_trigger_encode():
    p = Stick3Protocol()
    assert (
        p.scene_trigger_encode(1, 2, 3, 4, 5, 6)
        == b'Stick_3A\x6D\x00\x01\x00\x02\x03\x04\x00\x05\x00\x00\x00\x06\x00\x00\x00'
    )


def test_file_request_encode():
    p = Stick3Protocol()
    assert (
        p.file_request_encode('test.xml', 1, 512)
        == b'Stick_3A\x1f\x00test.xml' + b'\x00' * 24 + b'\x01\x00' + b'\x00\x02' + b'\x00\x00' + b'\x00' * 512
    )
    assert (
        p.file_request_encode('Show1/show_map.xml', 1, 512)
        == b'Stick_3A\x1f\x00\x53\x68\x6f\x77\x31\x2f\x73\x68\x6f\x77\x5f\x6d\x61\x70\x2e\x78\x6d\x6c'
        + b'\x00' * 14
        + b'\x01\x00'
        + b'\x00\x02'
        + b'\x00\x00'
        + b'\x00' * 512
    )


def test_zone_status_encode():
    p = Stick3Protocol()
    assert p.zone_status_encode(1, 2) == b'Stick_3A\x25\x00\x02\x00\x00\x00\x00\x00\x00\x00\x01\x00' + b'\x00' * 4


def test_poll_request_encode():
    p = Stick3Protocol()
    assert p.poll_request_encode() == b'LSAG_ALL\x00\x00\x12\x00\x00\x00\x00\x00'


def test_tcp_get_salt_encode():
    p = Stick3Protocol()
    assert p.tcp_get_salt_encode(1478522705698) == b'Stick_3A\x47\x00\x22\x17\xD2\x3E\x58\x01\x00\x00' + b'\x00' * 6


def test_tcp_authenticate_encode():
    p = Stick3Protocol()

    assert (
        p.tcp_authenticate_encode(1478522705698, b'remote', b'z' * 32, b'x' * 32)
        == b'Stick_3A\x48\x00\x22\x17\xD2\x3E\x58\x01\x00\x00'
        + b'remote'
        + b'\x00' * 26
        + b'z' * 32
        + b'x' * 32
        + b'\x00' * 6
    )


def test_auth_message_encode():
    p = Stick3Protocol()
    assert p.auth_message_encode(b'LSAG_ALL', 0x48, 1478522705698, b'remote', b'z' * 32) == (
        b'LSAG_ALL\x48\x00\x22\x17\xD2\x3E\x58\x01\x00\x00' + b'remote' + b'\x00' * 26 + b'z' * 32
    )
