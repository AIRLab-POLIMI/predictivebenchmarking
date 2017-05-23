// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpFrontierElement = require('./ExpFrontierElement.js');

//-----------------------------------------------------------

class ExpFrontier {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.frontier_element = null;
    }
    else {
      if (initObj.hasOwnProperty('frontier_element')) {
        this.frontier_element = initObj.frontier_element
      }
      else {
        this.frontier_element = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExpFrontier
    // Serialize message field [frontier_element]
    // Serialize the length for message field [frontier_element]
    bufferOffset = _serializer.uint32(obj.frontier_element.length, buffer, bufferOffset);
    obj.frontier_element.forEach((val) => {
      bufferOffset = ExpFrontierElement.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExpFrontier
    let len;
    let data = new ExpFrontier(null);
    // Deserialize message field [frontier_element]
    // Deserialize array length for message field [frontier_element]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.frontier_element = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.frontier_element[i] = ExpFrontierElement.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.frontier_element.forEach((val) => {
      length += ExpFrontierElement.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/ExpFrontier';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a022dc7f2d36765e856b2878d8a5476f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ExpFrontierElement[] frontier_element
    
    ================================================================================
    MSG: adhoc_communication/ExpFrontierElement
    int64 id
    string detected_by_robot_str
    int64 detected_by_robot
    float64 robot_home_position_x
    float64 robot_home_position_y
    float64 x_coordinate
    float64 y_coordinate
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ExpFrontier(null);
    if (msg.frontier_element !== undefined) {
      resolved.frontier_element = new Array(msg.frontier_element.length);
      for (let i = 0; i < resolved.frontier_element.length; ++i) {
        resolved.frontier_element[i] = ExpFrontierElement.Resolve(msg.frontier_element[i]);
      }
    }
    else {
      resolved.frontier_element = []
    }

    return resolved;
    }
};

module.exports = ExpFrontier;
