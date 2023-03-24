FROM ros:noetic-ros-core

RUN apt-get update
RUN apt-get install -y git
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc


RUN mkdir -p /home/catkin_ws/src
WORKDIR /home/catkin_ws/src

#RUN git clone https://github.com/voltbro/ros_book_samples
COPY . ./ros_book_samples
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; catkin_init_workspace'

RUN python3 --version
RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN apt-get install -y python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
RUN apt-get install -y ros-noetic-catkin python3-catkin-tools python3-catkin-pkg


WORKDIR /home/catkin_ws
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /home/catkin_ws; catkin_make'
RUN echo "source /home/catkin_ws/devel/setup.bash" >> ~/.bashrc

WORKDIR /home/catkin_ws/src/ros_book_samples
RUN chmod +x entrypoints/two_ints_client.sh
RUN chmod +x entrypoints/two_ints_server.sh

RUN chmod +x entrypoints/topic_subscriber.sh
RUN chmod +x entrypoints/topic_publisher.sh

RUN chmod +x entrypoints/roscore.sh