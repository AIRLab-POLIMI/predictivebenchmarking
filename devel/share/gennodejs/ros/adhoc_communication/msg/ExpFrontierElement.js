// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ExpFrontierElement {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.detected_by_robot_str = null;
      this.detected_by_robot = null;
      this.robot_home_position_x = null;
      this.robot_home_position_y = null;
      this.x_coordinate = null;
      this.y_coordinate = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('detected_by_robot_str')) {
        this.detected_by_robot_str = initObj.detected_by_robot_str
      }
      else {
        this.detected_by_robot_str = '';
      }
      if (initObj.hasOwnProperty('detected_by_robot')) {
        this.detected_by_robot = initObj.detected_by_robot
      }
      else {
        this.detected_by_robot = 0;
      }
      if (initObj.hasOwnProperty('robot_home_position_x')) {
        this.robot_home_position_x = initObj.robot_home_position_x
      }
      else {
        this.robot_home_position_x = 0.0;
      }
      if (initObj.hasOwnProperty('robot_home_position_y')) {
        this.robot_home_position_y = initObj.robot_home_position_y
      }
      else {
        this.robot_home_position_y = 0.0;
      }
      if (initObj.hasOwnProperty('x_coordinate')) {
        this.x_coordinate = initObj.x_coordinate
      }
      else {
        this.x_coordinate = 0.0;
      }
      if (initObj.hasOwnProperty('y_coordinate')) {
        this.y_coordinate = initObj.y_coordinate
      }
      else {
        this.y_coordinate = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExpFrontierElement
    // Serialize message field [id]
    bufferOffset = _serializer.int64(obj.id, buffer, bufferOffset);
    // Serialize message field [detected_by_robot_str]
    bufferOffset = _serializer.string(obj.detected_by_robot_str, buffer, bufferOffset);
    // Serialize message field [detected_by_robot]
    bufferOffset = _serializer.int64(obj.detected_by_robot, buffer, bufferOffset);
    // Serialize message field [robot_home_position_x]
    bufferOffset = _serializer.float64(obj.robot_home_position_x, buffer, bufferOffset);
    // Serialize message field [robot_home_position_y]
    bufferOffset = _serializer.float64(obj.robot_home_position_y, buffer, bufferOffset);
    // Serialize message field [x_coordinate]
    bufferOffset = _serializer.float64(obj.x_coordinate, buffer, bufferOffset);
    // Serialize message field [y_coordinate]
    bufferOffset = _serializer.float64(obj.y_coordinate, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExpFrontierElement
    let len;
    let data = new ExpFrontierElement(null);
    // Deserialize message field [id]
    data.id = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [detected_by_robot_str]
    data.detected_by_robot_str = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [detected_by_robot]
    data.detected_by_robot = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [robot_home_position_x]
    data.robot_home_position_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [robot_home_position_y]
    data.robot_home_position_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [x_coordinate]
    data.x_coordinate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y_coordinate]
    data.y_coordinate = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.detected_by_robot_str.length;
    return length + 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/ExpFrontierElement';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a783300e6ed76ebb52feb001fc044546';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new ExpFrontierElement(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.detected_by_robot_str !== undefined) {
      resolved.detected_by_robot_str = msg.detected_by_robot_str;
    }
    else {
      resolved.detected_by_robot_str = ''
    }

    if (msg.detected_by_robot !== undefined) {
      resolved.detected_by_robot = msg.detected_by_robot;
    }
    else {
      resolved.detected_by_robot = 0
    }

    if (msg.robot_home_position_x !== undefined) {
      resolved.robot_home_position_x = msg.robot_home_position_x;
    }
    else {
      resolved.robot_home_position_x = 0.0
    }

    if (msg.robot_home_position_y !== undefined) {
      resolved.robot_home_position_y = msg.robot_home_position_y;
    }
    else {
      resolved.robot_home_position_y = 0.0
    }

    if (msg.x_coordinate !== undefined) {
      resolved.x_coordinate = msg.x_coordinate;
    }
    else {
      resolved.x_coordinate = 0.0
    }

    if (msg.y_coordinate !== undefined) {
      resolved.y_coordinate = msg.y_coordinate;
    }
    else {
      resolved.y_coordinate = 0.0
    }

    return resolved;
    }
};

module.exports = ExpFrontierElement;
