"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Point3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    D_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    d: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
        z: builtins.float | None = ...,
        d: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["d", b"d", "x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["d", b"d", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Point3 = Point3

@typing_extensions.final
class Vector3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    D_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    d: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
        z: builtins.float | None = ...,
        d: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["d", b"d", "x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["d", b"d", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Vector3 = Vector3

@typing_extensions.final
class Vector4(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    W_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    w: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
        z: builtins.float | None = ...,
        w: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["w", b"w", "x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["w", b"w", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Vector4 = Vector4

@typing_extensions.final
class Quat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    W_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    w: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
        z: builtins.float | None = ...,
        w: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["w", b"w", "x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["w", b"w", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Quat = Quat

@typing_extensions.final
class Transform(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROTATION_FIELD_NUMBER: builtins.int
    TRANSLATION_FIELD_NUMBER: builtins.int
    SCALE_FIELD_NUMBER: builtins.int
    @property
    def rotation(self) -> global___Quat: ...
    @property
    def translation(self) -> global___Vector3: ...
    @property
    def scale(self) -> global___Vector3: ...
    def __init__(
        self,
        *,
        rotation: global___Quat | None = ...,
        translation: global___Vector3 | None = ...,
        scale: global___Vector3 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rotation", b"rotation", "scale", b"scale", "translation", b"translation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["rotation", b"rotation", "scale", b"scale", "translation", b"translation"]) -> None: ...

global___Transform = Transform

@typing_extensions.final
class Matrix4(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    M00_FIELD_NUMBER: builtins.int
    M01_FIELD_NUMBER: builtins.int
    M02_FIELD_NUMBER: builtins.int
    M03_FIELD_NUMBER: builtins.int
    M10_FIELD_NUMBER: builtins.int
    M11_FIELD_NUMBER: builtins.int
    M12_FIELD_NUMBER: builtins.int
    M13_FIELD_NUMBER: builtins.int
    M20_FIELD_NUMBER: builtins.int
    M21_FIELD_NUMBER: builtins.int
    M22_FIELD_NUMBER: builtins.int
    M23_FIELD_NUMBER: builtins.int
    M30_FIELD_NUMBER: builtins.int
    M31_FIELD_NUMBER: builtins.int
    M32_FIELD_NUMBER: builtins.int
    M33_FIELD_NUMBER: builtins.int
    m00: builtins.float
    m01: builtins.float
    m02: builtins.float
    m03: builtins.float
    m10: builtins.float
    m11: builtins.float
    m12: builtins.float
    m13: builtins.float
    m20: builtins.float
    m21: builtins.float
    m22: builtins.float
    m23: builtins.float
    m30: builtins.float
    m31: builtins.float
    m32: builtins.float
    m33: builtins.float
    def __init__(
        self,
        *,
        m00: builtins.float | None = ...,
        m01: builtins.float | None = ...,
        m02: builtins.float | None = ...,
        m03: builtins.float | None = ...,
        m10: builtins.float | None = ...,
        m11: builtins.float | None = ...,
        m12: builtins.float | None = ...,
        m13: builtins.float | None = ...,
        m20: builtins.float | None = ...,
        m21: builtins.float | None = ...,
        m22: builtins.float | None = ...,
        m23: builtins.float | None = ...,
        m30: builtins.float | None = ...,
        m31: builtins.float | None = ...,
        m32: builtins.float | None = ...,
        m33: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["m00", b"m00", "m01", b"m01", "m02", b"m02", "m03", b"m03", "m10", b"m10", "m11", b"m11", "m12", b"m12", "m13", b"m13", "m20", b"m20", "m21", b"m21", "m22", b"m22", "m23", b"m23", "m30", b"m30", "m31", b"m31", "m32", b"m32", "m33", b"m33"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["m00", b"m00", "m01", b"m01", "m02", b"m02", "m03", b"m03", "m10", b"m10", "m11", b"m11", "m12", b"m12", "m13", b"m13", "m20", b"m20", "m21", b"m21", "m22", b"m22", "m23", b"m23", "m30", b"m30", "m31", b"m31", "m32", b"m32", "m33", b"m33"]) -> None: ...

global___Matrix4 = Matrix4