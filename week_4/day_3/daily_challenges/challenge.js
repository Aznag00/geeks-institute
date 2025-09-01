class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }
  watch() {
    console.log(
      `${this.uploader} watched all ${this.time} seconds of "${this.title}"!`
    );
  }
}

const Video1 = new Video("python course", "mehdi", 150);
Video1.watch();
const video2 = new Video("flask course", "ahmed", 200);
video2.watch();

const videosData = [
  { title: "node.js tutorial", uploader: "ali", time: 420 },
  { title: "css guide", uploader: "yassin", time: 250 },
  { title: "html course", uploader: "omar", time: 180 },
  { title: "postgresql basics", uploader: "mohammed", time: 500 },
];

const videos = [];

videosData.forEach((data) => {
  const video = new Video(data.title, data.uploader, data.time);
  videos.push(video);
  video.watch();
});
