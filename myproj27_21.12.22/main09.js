const { melon_data: song_array } = require("./melon_data");


// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

// 좋아요 수로만 필터링 ~ 
// 그러면 좋아요 수 - like만 가져와서 ?
// like > 200_000 


const filtered_title_array = song_array
    .filter(({ like }) => like >= 200_000)
    .map(({ title }) => title);


for (const title of filtered_title_array) {
    console.log(title);
}
