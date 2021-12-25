import { useState } from 'react';
import initialVideoList from 'components/data/song_list_v2.json';
import React from 'react';
import ReactPlayer from 'react-player/youtube';
import { YoutubeOutlined } from '@ant-design/icons';
import { Avatar, Input, List, Typography, notification } from 'antd';

function PlayList() {
  const [videoList, setVideoList] = useState([]);
  const [youtubeUrl, setYoutubeUrl] = useState([]);
  const handleClick = () => {
    setVideoList(initialVideoList);
  };
  console.log(videoList);

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>
        <YoutubeOutlined />
        Youtube PlayList
      </h2>
      <button onClick={handleClick}>로딩</button>

      <ul>
        {videoList.map((video) => {
          return (
            <div key={video.title} onClick={() => setYoutubeUrl(video.url)}>
              <h3>{video.title}</h3>
              <img src={video.thumbnail_url} />
              <ReactPlayer width="640px" height="360px" url={video.url} />
            </div>
          );
        })}
      </ul>
    </div>
  );
}

export default PlayList;
