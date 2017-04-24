####### Compiler, tools and options

CXX      = g++
CXXFLAGS = -pipe -g -Wall -W -O2 -ansi -pedantic
INCPATH  = -I.
LINK     = g++
LFLAGS   = 
RM	 = rm -f

####### Files

SOURCES = metricEvaluator.cpp \
		logutil.cpp \
		linalg/vectorFromString.cpp \
		linalg/stringTools.cpp \
		linalg/runtimeError.cpp

OBJECTS = $(SOURCES:.cpp=.o)

TARGET   = metricEvaluator

####### Build rules

%.o: %.cpp
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $@ $<

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OBJECTS)

clean:
	$(RM) $(OBJECTS)

####### depends

metricEvaluator.o: metricEvaluator.cpp linalg/matrix4x4.h \
		linalg/vectorFromString.h \
		statistics.h \
		structs.h \
		linalg/matrix.h \
		linalg/matrix3x3.h \
		linalg/vector3.h \
		linalg/vector.h

logutil.o: logutil.cpp logutil.h structs.h

linalg/vectorFromString.o: linalg/vectorFromString.cpp linalg/vectorFromString.h \
		linalg/stringTools.h \
		linalg/vector.h \
		linalg/runtimeError.h

linalg/stringTools.o: linalg/stringTools.cpp linalg/stringTools.h \
		linalg/runtimeError.h

linalg/runtimeError.o: linalg/runtimeError.cpp linalg/runtimeError.h
