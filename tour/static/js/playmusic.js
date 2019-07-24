function playmusic(obj) {
    var player = document.getElementById('player');

    if(player.paused){
        player.play();
        obj.src = '/static/img/musicBtn.png';
    }else{
        player.pause();
        obj.src = '/static/img/musicBtnoff.png'
    }
}