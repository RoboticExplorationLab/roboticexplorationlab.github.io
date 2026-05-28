---
layout: default
title: Courses
---

<style>
.yt-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:12px 0}
.yt-card{border-radius:6px;overflow:hidden;background:#111}
.yt-thumb{position:relative;width:100%;padding-top:56.25%;cursor:pointer}
.yt-thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.yt-thumb .yt-play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.2);transition:background .15s}
.yt-thumb .yt-play:hover{background:rgba(0,0,0,.45)}
.yt-thumb .yt-play svg{width:44px;height:44px}
.yt-thumb iframe{position:absolute;inset:0;width:100%;height:100%;border:none}
.yt-title{padding:7px 10px 9px;font-size:12px;color:#ddd;line-height:1.4;background:#181818}
</style>

<script>
function buildYtGrid(gridId, playlistId, videoIds) {
  var g = document.getElementById(gridId);
  if (!g) return;
  videoIds.forEach(function(id, i) {
    var card  = document.createElement("div"); card.className = "yt-card";
    var thumb = document.createElement("div"); thumb.className = "yt-thumb";
    var img   = document.createElement("img");
    img.src = "https://i.ytimg.com/vi/" + id + "/mqdefault.jpg";
    img.alt = ""; img.loading = "lazy";
    var play  = document.createElement("div"); play.className = "yt-play";
    play.innerHTML = '<svg viewBox="0 0 68 48" xmlns="http://www.w3.org/2000/svg"><path d="M66.5 7.7a8.5 8.5 0 0 0-6-6C56 0 34 0 34 0S12 0 7.5 1.7a8.5 8.5 0 0 0-6 6A89 89 0 0 0 0 24a89 89 0 0 0 1.5 16.3 8.5 8.5 0 0 0 6 6C12 48 34 48 34 48s22 0 26.5-1.7a8.5 8.5 0 0 0 6-6A89 89 0 0 0 68 24a89 89 0 0 0-1.5-16.3z" fill="#f00"/><path d="M27 34l18-10-18-10z" fill="#fff"/></svg>';
    play.onclick = function() {
      var fr = document.createElement("iframe");
      fr.src = "https://www.youtube.com/embed/" + id + "?list=" + playlistId + "&autoplay=1";
      fr.allow = "accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture";
      fr.allowFullscreen = true;
      thumb.innerHTML = ""; thumb.appendChild(fr);
    };
    thumb.appendChild(img); thumb.appendChild(play);
    var title = document.createElement("div"); title.className = "yt-title";
    title.textContent = "Video " + (i + 1);
    fetch("https://noembed.com/embed?url=https://www.youtube.com/watch?v=" + id)
      .then(function(r) { return r.json(); })
      .then(function(d) { if (d.title) title.textContent = d.title; })
      .catch(function() {});
    card.appendChild(thumb); card.appendChild(title); g.appendChild(card);
  });
}
</script>

## Optimal Control and Reinforcement Learning

<div class="span9">
  <div class="yt-grid" id="grid-ocrl"></div>
</div><!--/span-->

<script>
buildYtGrid("grid-ocrl", "PLZnJoM76RM6IAJfMXd1PgGNXn3dxhkVgI", [
  "SvAYJC7jug8","s_Ubs6NUVBQ","b9xRcX5XQXE","7qG3kxOHpW0","QvVCj7qRWaQ",
  "TmxUlQjMTew","kG3Cv68u1Wc","oC3wqK6GKFA","H1QNYYBbYOI","EJ7UXxQKVfE",
  "9zNovzAIMhY","pXhcPaVN8mE","6J_OGtCOPMw","Y5bqxWMi_vc","v5Ip49OROGE",
  "Lk7JxJFhvME","nRp3HLHBV9A","5wuHIqwKCXA","mFjY98sOqYM","WLaEiWtKriQ"
]);
</script>

## Spacecraft Attitude Determination and Control

<div class="span9">
  <div class="yt-grid" id="grid-sadc"></div>
</div><!--/span-->

<script>
buildYtGrid("grid-sadc", "PLZnJoM76RM6L4_G7ViuutMNxEqNL_IOYg", [
  "nIcKB5hmtVU","I8q6DFQH8_c","DJM6EGjsVNY","N6GxcDMYjfc","yXTRo3Fd1S0",
  "kWxkK4gqmcg","gMFPXy0ORMM","zY4ZqGm3Dew","6Fxvr4NXMX8","XL5ew9WCPYE",
  "fBxqpPlrBBM","eBNXVH5KMPM","o5NWBFEOroM","BxRhK5R8AQA","HHqrIGRtDj4",
  "4JvYXVbBPio","vlOGXhkLjVk","CUOODp6OIUA","sSwKN2vTuaM","Ow5NBvqS2v0",
  "TpNBxNm7Jhk","KyxZDXkQEGc","FhGbPPHLmO4","3WHq5AZ_VPU","dODNRYoGJP0"
]);
</script>
