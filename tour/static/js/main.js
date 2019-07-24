window.onload = function () {
    var url = window.location.href
    url = decodeURI(url)
    var urllist = url.split('=')
    if(jQuery.isEmptyObject(urllist[1])){
        document.getElementById('user').innerHTML = 'unlogin'
    }
    else{
        document.getElementById('user').innerHTML = urllist[1]
    }


        setInterval(function () {
    var date = new Date()
    var h = date.getHours()
    var m = date.getMinutes()
    var s = date.getSeconds()
    if(h<10){
        h = '0'+h
    }
    if(m<10){
        m = '0'+m
    }
    if(s<10){
        s= '0'+s
    }

    document.getElementById('timetxt').innerHTML = h+':'+m+':'+s
    },1000)

    $.ajax({
        type : 'get',
        url:'http://127.0.0.1:8000/getallzone',
        async: true,
        timeout: 3000,
        dataType: 'json',
        success:function (data) {
            // alert(data)
            for(var i in data){
                addhistory(data[i])
            }
        },
        error:function () {
            alert('请求失败！')
        }
    })
}
function sendData() {
    var dataform = new FormData($("#datafrom")[0])
    console.log(dataform)
    var user = document.getElementById('user').innerHTML;
    dataform.append("username", user)
    var dates = new Date()
    var y = dates.getFullYear()
    var m = dates.getMonth() + 1
    var d = dates.getDate()
    dataform.append('sendtime',y+"/"+m+"/"+d)
    //追加时间戳
    dataform.append('times', dates.getTime())
    $.ajax({
        type: 'post',
        url: 'http://127.0.0.1:8000/sendZone',
        data: dataform,
        async: true,
        dataType: 'json',
        timeout: 5000,
        cache: false,
        contentType:false,
        processData: false,
        success:function (data) {
            // alert(data);
            if(data.code == '1'){
                alert('添加成功！')
                var player =document.getElementById("player")
				if (!jQuery.isEmptyObject(data.musicname)) {
					player.src = data.musicname
				}
                addhistory(data)
            }
            if(data.code == '0'){
                alert('添加失败！')
            }
        },
        error:function () {
            alert('请求异常！！')
        }
    })
}
function addhistory(data) {
    //动态生成item
    var $ul = document.getElementById('ulitem')
    var $li = document.createElement('li')

    data.musicname = decodeURI(data.musicname)
    st = data.musicname.split('/')
    // $ul.appendChild($li)
    $ul.insertBefore($li,$ul.firstChild)
    $li.className = 'item'
    $li.innerHTML = '<li class="item">\n' +
        '<img class="item-img" src="'+data.photoname+'"/>\n' +
        '<div class="item-right">\n' +
        // '<a class="delete" href="#">删除</a>\n' +
        '<p class="itemtxt">'+data.sendtxt+'</p>\n' +
        '<div class="userbox"><img class="icon-img" src="/static/img/a1.png"/> ' +
        '<span class="username">'+data.username+'</span><span class="sendtime">'+data.sendtime+'</span></div>\n' +
        // '<div><a class="musicname" href="#">'+st[3]+'</a></div>\n' +
        '</div>\n' +
        '</li>'
}
