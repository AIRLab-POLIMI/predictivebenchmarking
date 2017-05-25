// Generated by gencpp from file adhoc_communication/MmPoint.msg
// DO NOT EDIT!


#ifndef ADHOC_COMMUNICATION_MESSAGE_MMPOINT_H
#define ADHOC_COMMUNICATION_MESSAGE_MMPOINT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace adhoc_communication
{
template <class ContainerAllocator>
struct MmPoint_
{
  typedef MmPoint_<ContainerAllocator> Type;

  MmPoint_()
    : src_robot()
    , x(0.0)
    , y(0.0)  {
    }
  MmPoint_(const ContainerAllocator& _alloc)
    : src_robot(_alloc)
    , x(0.0)
    , y(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _src_robot_type;
  _src_robot_type src_robot;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;




  typedef boost::shared_ptr< ::adhoc_communication::MmPoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::adhoc_communication::MmPoint_<ContainerAllocator> const> ConstPtr;

}; // struct MmPoint_

typedef ::adhoc_communication::MmPoint_<std::allocator<void> > MmPoint;

typedef boost::shared_ptr< ::adhoc_communication::MmPoint > MmPointPtr;
typedef boost::shared_ptr< ::adhoc_communication::MmPoint const> MmPointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::adhoc_communication::MmPoint_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::adhoc_communication::MmPoint_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace adhoc_communication

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'adhoc_communication': ['/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::MmPoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::MmPoint_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::MmPoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::MmPoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::MmPoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::MmPoint_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::adhoc_communication::MmPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bf827d01cbf6a28b70ad364cdc656d65";
  }

  static const char* value(const ::adhoc_communication::MmPoint_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbf827d01cbf6a28bULL;
  static const uint64_t static_value2 = 0x70ad364cdc656d65ULL;
};

template<class ContainerAllocator>
struct DataType< ::adhoc_communication::MmPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adhoc_communication/MmPoint";
  }

  static const char* value(const ::adhoc_communication::MmPoint_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::adhoc_communication::MmPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string src_robot\n\
float64 x\n\
float64 y\n\
";
  }

  static const char* value(const ::adhoc_communication::MmPoint_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::adhoc_communication::MmPoint_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.src_robot);
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MmPoint_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::adhoc_communication::MmPoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::adhoc_communication::MmPoint_<ContainerAllocator>& v)
  {
    s << indent << "src_robot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.src_robot);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ADHOC_COMMUNICATION_MESSAGE_MMPOINT_H
