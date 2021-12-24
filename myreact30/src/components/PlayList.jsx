import { useState } from 'react';
import initialVideoList from 'components/data/song_list_v2.json';
import React from 'react';
import ReactPlayer from 'react-player/youtube';
import { Avatar, Input, List, Typography, notification, Divider } from 'antd';

function PlayList() {
  const [videoList, setVideoList] = useState([]);
  const handleClick = () => {
    setVideoList(initialVideoList);
  };
  console.log(videoList);

  return (
    <div>
      <h2>Youtube PlayList </h2>
      <button onClick={handleClick}>로딩</button>

      <ul>
        {videoList.map((video) => {
          return (
            <ul>
              <li>{video.title}</li>
              <li>
                <ReactPlayer width="640px" height="360px" url={video.url} />
              </li>
              <p></p>
            </ul>
          );
        })}
      </ul>
    </div>
  );
}

export default PlayList;
