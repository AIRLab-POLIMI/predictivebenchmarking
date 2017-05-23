// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let nav_msgs = _finder('nav_msgs');

//-----------------------------------------------------------

class MmMapUpdate {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.src_robot = null;
      this.update_numbers = null;
      this.map = null;
    }
    else {
      if (initObj.hasOwnProperty('src_robot')) {
        this.src_robot = initObj.src_robot
      }
      else {
        this.src_robot = '';
      }
      if (initObj.hasOwnProperty('update_numbers')) {
        this.update_numbers = initObj.update_numbers
      }
      else {
        this.update_numbers = [];
      }
      if (initObj.hasOwnProperty('map')) {
        this.map = initObj.map
      }
      else {
        this.map = new nav_msgs.msg.OccupancyGrid();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MmMapUpdate
    // Serialize message field [src_robot]
    bufferOffset = _serializer.string(obj.src_robot, buffer, bufferOffset);
    // Serialize message field [update_numbers]
    bufferOffset = _arraySerializer.int32(obj.update_numbers, buffer, bufferOffset, null);
    // Serialize message field [map]
    bufferOffset = nav_msgs.msg.OccupancyGrid.serialize(obj.map, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MmMapUpdate
    let len;
    let data = new MmMapUpdate(null);
    // Deserialize message field [src_robot]
    data.src_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [update_numbers]
    data.update_numbers = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [map]
    data.map = nav_msgs.msg.OccupancyGrid.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.src_robot.length;
    length += 4 * object.update_numbers.length;
    length += nav_msgs.msg.OccupancyGrid.getMessageSize(object.map);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/MmMapUpdate';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cf3b81cd59c0d2ac72a16d2e10428027';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string src_robot
    int32[] update_numbers
    nav_msgs/OccupancyGrid map
    
    ================================================================================
    MSG: nav_msgs/OccupancyGrid
    # This represents a 2-D grid map, in which each cell represents the probability of
    # occupancy.
    
    Header header 
    
    #MetaData for the map
    MapMetaData info
    
    # The map data, in row-major order, starting with (0,0).  Occupancy
    # probabilities are in the range [0,100].  Unknown is -1.
    int8[] data
    
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
    MSG: nav_msgs/MapMetaData
    # This hold basic information about the characterists of the OccupancyGrid
    
    # The time at which the map was loaded
    time map_load_time
    # The map resolution [m/cell]
    float32 resolution
    # Map width [cells]
    uint32 width
    # Map height [cells]
    uint32 height
    # The origin of the map [m, m, rad].  This is the real-world pose of the
    # cell (0,0) in the map.
    geometry_msgs/Pose origin
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
    const resolved = new MmMapUpdate(null);
    if (msg.src_robot !== undefined) {
      resolved.src_robot = msg.src_robot;
    }
    else {
      resolved.src_robot = ''
    }

    if (msg.update_numbers !== undefined) {
      resolved.update_numbers = msg.update_numbers;
    }
    else {
      resolved.update_numbers = []
    }

    if (msg.map !== undefined) {
      resolved.map = nav_msgs.msg.OccupancyGrid.Resolve(msg.map)
    }
    else {
      resolved.map = new nav_msgs.msg.OccupancyGrid()
    }

    return resolved;
    }
};

module.exports = MmMapUpdate;
