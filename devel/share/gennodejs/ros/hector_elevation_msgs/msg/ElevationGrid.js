// Auto-generated. Do not edit!

// (in-package hector_elevation_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ElevationMapMetaData = require('./ElevationMapMetaData.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ElevationGrid {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.info = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('info')) {
        this.info = initObj.info
      }
      else {
        this.info = new ElevationMapMetaData();
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ElevationGrid
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [info]
    bufferOffset = ElevationMapMetaData.serialize(obj.info, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.int16(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ElevationGrid
    let len;
    let data = new ElevationGrid(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [info]
    data.info = ElevationMapMetaData.deserialize(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.int16(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 2 * object.data.length;
    return length + 110;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hector_elevation_msgs/ElevationGrid';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '13f6dd2a4434f89ebecd8bfafa38cdf1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # This represents a 2-D grid map, in which each cell represents the elevation.
    
    Header header 
    
    #MetaData for the map
    ElevationMapMetaData info
    
    # The map data, in row-major order, starting with (0,0).  Elevation values 
    # are in the range [0,32768].
    # -> 0 belongs to max negative elevation, 32767 to max positive elevation, "elevation_zero_level" coresponds to zero, -elevation_zero_level to unknown elevation
    int16[] data
    
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
    MSG: hector_elevation_msgs/ElevationMapMetaData
    # This hold basic information about the characterists of the EvaluationGrid
    
    # The time at which the map was loaded
    time map_load_time
    # Map resolution in xy plane [m/cell]
    float64 resolution_xy
    # Map resolution in height [m/cell]
    float64 resolution_z
    # min observed height [m]
    float64 min_elevation
    # max observed height [m]
    float64 max_elevation
    # Height zero value. For example 16384.
    int16 zero_elevation
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
    const resolved = new ElevationGrid(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.info !== undefined) {
      resolved.info = ElevationMapMetaData.Resolve(msg.info)
    }
    else {
      resolved.info = new ElevationMapMetaData()
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    return resolved;
    }
};

module.exports = ElevationGrid;
