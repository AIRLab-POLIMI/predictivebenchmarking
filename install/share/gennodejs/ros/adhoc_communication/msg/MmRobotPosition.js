// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class MmRobotPosition {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.src_robot = null;
      this.position = null;
    }
    else {
      if (initObj.hasOwnProperty('src_robot')) {
        this.src_robot = initObj.src_robot
      }
      else {
        this.src_robot = '';
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new geometry_msgs.msg.PoseStamped();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MmRobotPosition
    // Serialize message field [src_robot]
    bufferOffset = _serializer.string(obj.src_robot, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.position, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MmRobotPosition
    let len;
    let data = new MmRobotPosition(null);
    // Deserialize message field [src_robot]
    data.src_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.src_robot.length;
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.position);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/MmRobotPosition';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b110eae90e8648401835f8c826926f86';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string src_robot
    geometry_msgs/PoseStamped position
    
    ================================================================================
    MSG: geometry_msgs/PoseStamped
    # A Pose with reference coordinate frame and timestamp
    Header header
    Pose pose
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MmRobotPosition(null);
    if (msg.src_robot !== undefined) {
      resolved.src_robot = msg.src_robot;
    }
    else {
      resolved.src_robot = ''
    }

    if (msg.position !== undefined) {
      resolved.position = geometry_msgs.msg.PoseStamped.Resolve(msg.position)
    }
    else {
      resolved.position = new geometry_msgs.msg.PoseStamped()
    }

    return resolved;
    }
};

module.exports = MmRobotPosition;
