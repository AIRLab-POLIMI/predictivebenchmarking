// Auto-generated. Do not edit!

// (in-package explorer.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Speed {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.avg_speed = null;
    }
    else {
      if (initObj.hasOwnProperty('avg_speed')) {
        this.avg_speed = initObj.avg_speed
      }
      else {
        this.avg_speed = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Speed
    // Serialize message field [avg_speed]
    bufferOffset = _serializer.float32(obj.avg_speed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Speed
    let len;
    let data = new Speed(null);
    // Deserialize message field [avg_speed]
    data.avg_speed = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'explorer/Speed';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ab71c17b247789c29752d16cf36898a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 avg_speed
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Speed(null);
    if (msg.avg_speed !== undefined) {
      resolved.avg_speed = msg.avg_speed;
    }
    else {
      resolved.avg_speed = 0.0
    }

    return resolved;
    }
};

module.exports = Speed;
