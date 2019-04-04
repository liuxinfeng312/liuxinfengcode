import requests
from bs4 import BeautifulSoup
html='''

<html xmlns="http://www.w3.org/1999/xhtml"><head>
    <title>GY0-【国际业务部】Senior Web Developer（Hong Kong） | 社会招聘 | Tencent 腾讯招聘</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <!-- Js Css -->
    	<link media="screen" href="//cdn.m.tencent.com/hr_static/css/all.css?max_age=86412" type="text/css" rel="stylesheet">
	<script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/jquery-1.7.2.min.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/jquery-ui-1.7.2.custom.min.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/thickbox.js"></script>
    <link media="screen" href="//cdn.m.tencent.com/hr_static/css/thickbox.css" type="text/css" rel="stylesheet">
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/functions.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/utils.js"></script>
    <script language="javascript" src="//vm.gtimg.cn/tencentvideo/txp/js/txplayer.js" charset="utf-8"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/all.js?max_age=86412"></script>    <!-- Js Css -->
<style type="text/css" abt="234"></style><script src="http://static.bshare.cn/b/components/bsStatic.js?v=20150603" type="text/javascript" charset="utf-8"></script><script src="http://static.bshare.cn/b/engines/bs-engine.js?v=20150603" type="text/javascript" charset="utf-8"></script><script>//console.log('a')
</script><script>//remove 17173 video ad
doAdblock();
function doAdblock(){
    (function() {
        function A() {}
        A.prototype = {
            rules: {
                '17173_in':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFile(Customer)?\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_in_20150522.swf"
                },
                '17173_out':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/PreloaderFileFirstpage\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_out_20150522.swf"
                },
                '17173_live':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream(_firstpage)?\.swf/,
                    'replace':"http://swf.adtchrome.com/17173_stream_20150522.swf"
                },
                '17173_live_out':{
                    'find':/http:\/\/f\.v\.17173cdn\.com\/(\d+\/)?flash\/Player_stream_(custom)?Out\.swf/,
                    'replace':"http://swf.adtchrome.com/17173.out.Live.swf"
                }
            },
            _done: null,
            get done() {
                if(!this._done) {
                    this._done = new Array();
                }
                return this._done;
            },
            addAnimations: function() {
                var style = document.createElement('style');
                style.type = 'text/css';
                style.innerHTML = 'object,embed{\
                -webkit-animation-duration:.001s;-webkit-animation-name:playerInserted;\
                -ms-animation-duration:.001s;-ms-animation-name:playerInserted;\
                -o-animation-duration:.001s;-o-animation-name:playerInserted;\
                animation-duration:.001s;animation-name:playerInserted;}\
                @-webkit-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @-ms-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @-o-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}\
                @keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}';
                document.getElementsByTagName('head')[0].appendChild(style);
            },
            animationsHandler: function(e) {
                if(e.animationName === 'playerInserted') {
                    this.replace(e.target);
                }
            },
            replace: function(elem) {
                if(this.done.indexOf(elem) != -1) return;
                this.done.push(elem);
                var player = elem.data || elem.src;
                if(!player) return;
                var i, find, replace = false;
                for(i in this.rules) {
                    find = this.rules[i]['find'];
                    if(find.test(player)) {
                        replace = this.rules[i]['replace'];
                        if('function' === typeof this.rules[i]['preHandle']) {
                            this.rules[i]['preHandle'].bind(this, elem, find, replace, player)();
                        }else{
                            this.reallyReplace.bind(this, elem, find, replace)();
                        }
                        break;
                    }
                }
            },
            reallyReplace: function(elem, find, replace) {
                elem.data && (elem.data = elem.data.replace(find, replace)) || elem.src && ((elem.src = elem.src.replace(find, replace)) && (elem.style.display = 'block'));
                var b = elem.querySelector("param[name='movie']");
                this.reloadPlugin(elem);
            },
            reloadPlugin: function(elem) {
                var nextSibling = elem.nextSibling;
                var parentNode = elem.parentNode;
                parentNode.removeChild(elem);
                var newElem = elem.cloneNode(true);
                this.done.push(newElem);
                if(nextSibling) {
                    parentNode.insertBefore(newElem, nextSibling);
                } else {
                    parentNode.appendChild(newElem);
                }
            },
            init: function() {
                var handler = this.animationsHandler.bind(this);
                document.body.addEventListener('webkitAnimationStart', handler, false);
                document.body.addEventListener('msAnimationStart', handler, false);
                document.body.addEventListener('oAnimationStart', handler, false);
                document.body.addEventListener('animationstart', handler, false);
                this.addAnimations();
            }
        };
        new A().init();
    })();
}
//remove baidu search ad
if(document.URL.indexOf('www.baidu.com') >= 0){
    if(document && document.getElementsByTagName && document.getElementById && document.body){
        var aa = function(){
            var all = document.body.querySelectorAll("#content_left div,#content_left table");
            for(var i = 0; i < all.length; i++){
                if(/display:\s?(table|block)\s!important/.test(all[i].getAttribute("style"))){all[i].style.display= "none";all[i].style.visibility='hidden';}
            }
            all = document.body.querySelectorAll('.result.c-container[id="1"]');
            //if(all.length == 1) return;
            for(var i = 0; i < all.length; i++){
                if(all[i].innerHTML && all[i].innerHTML.indexOf('广告')>-1){
                    all[i].style.display= "none";all[i].style.visibility='hidden';
                }
            }
        }
        aa();
        document.getElementById('wrapper_wrapper').addEventListener('DOMSubtreeModified',aa)
    };
}
//remove sohu video ad
if (document.URL.indexOf("tv.sohu.com") >= 0){
    if (document.cookie.indexOf("fee_status=true")==-1){document.cookie='fee_status=true'};
}
//remove 56.com video ad
if (document.URL.indexOf("56.com") >= 0){
    if (document.cookie.indexOf("fee_status=true")==-1){document.cookie='fee_status=true'};
}
//fore iqiyi enable html5 player function
if (document.URL.indexOf("iqiyi.com") >= 0){
    if (document.cookie.indexOf("player_forcedType=h5_VOD")==-1){
        document.cookie='player_forcedType=h5_VOD'
        if(localStorage.reloadTime && Date.now() - parseInt(localStorage.reloadTime)<60000){
            console.log('no reload')
        }else{
            location.reload()
            localStorage.reloadTime = Date.now();
        }
    }
}
</script><style type="text/css">object,embed{                -webkit-animation-duration:.001s;-webkit-animation-name:playerInserted;                -ms-animation-duration:.001s;-ms-animation-name:playerInserted;                -o-animation-duration:.001s;-o-animation-name:playerInserted;                animation-duration:.001s;animation-name:playerInserted;}                @-webkit-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @-ms-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @-o-keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}                @keyframes playerInserted{from{opacity:0.99;}to{opacity:1;}}</style><style id="tsbrowser_video_independent_player_style" type="text/css">                                                            [tsbrowser_force_max_size] {                                                   width: 100% !important;                                                      height: 100% !important;                                                     left: 0px !important;                                                        top: 0px !important;                                                         margin: 0px !important;                                                      padding: 0px !important;                                                   }                                                                            [tsbrowser_force_fixed] {                                                      position: fixed !important;                                                  z-index: 9999 !important;                                                    background: black !important;                                              }                                                                            [tsbrowser_force_hidden] {                                                     opacity: 0 !important;                                                       z-index: 0 !important;                                                     }                                                                            [tsbrowser_hide_scrollbar] {                                                   overflow: hidden !important;                                               }</style></head>

<body>
	<div id="header">
    	<div class="maxwidth">
    		<a href="index.php" class="left" id="logo"><img src="//cdn.m.tencent.com/hr_static/img/logo.png"></a>
    		<div class="right" id="headertr">
    			<div class="right pl9" id="topshares">
    				<div class="shares">
    					<span class="left">分享到：</span>
		    			<!--<a href="javascript:;" onclick="shareto('qqt','top');" id="qqt" title="分享到腾讯微博">分享到腾讯微博</a>-->
		    			<a href="javascript:;" onclick="shareto('qzone','top');" id="qzone" title="分享到QQ空间">分享到QQ空间</a>
		    			<!--<a href="javascript:;" onclick="shareto('pengyou','top');" id="pengyou" title="分享到腾讯朋友">分享到腾讯朋友</a>-->
		    			<a href="javascript:;" onclick="shareto('sinat','top');" id="sinat" title="分享到新浪微博">分享到新浪微博</a>
		    			<!--<a href="javascript:;"  onclick="shareto('renren','top');"id="renren" title="分享到人人网">分享到人人网</a>-->
		    			<!--<a href="javascript:;"  onclick="shareto('kaixin001','top');"id="kaixin" title="分享到开心网">分享到开心网</a>-->
		    			<div class="clr"></div>
    				</div>
    				<!--<a href="javascript:;">分享</a>-->
    			</div>
    			<!--<div class="right pl9">-->
    				<!--<a href="http://t.qq.com/QQjobs" id="tqq" target="_blank">收听腾讯招聘</a>-->
    			<!--</div>-->
    			<div class="right pr9">
    				    				    					<a href="login.php" id="header_login_anchor">登录</a><span class="plr9">|</span><a href="reg.php">注册</a>
    				    				<span class="plr9">|</span><a href="question.php">反馈建议</a>
    				<span class="plr9">|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a>
    				<script>
    					var User_Account = "";
    				</script>
    				    			</div>
    			<div class="clr"></div>
    		</div>
    		<div class="clr"></div>
    	</div>
    	<div id="menus">
    		<div class="maxwidth">
	    		<ul id="menu" class="left">
	    			<li id="nav1"><a href="index.php">&nbsp;</a></li>
	    			<li id="nav2" class="active"><a href="social.php">&nbsp;</a></li>
	    			<li id="nav3"><a href="about.php">&nbsp;</a></li>
	    			<li id="nav4"><a href="workInTencent.php">&nbsp;</a></li>
	    		</ul>
	    		<a class="right texti9" target="_blank" id="navxy" href="http://join.qq.com">校园招聘</a>
	    		<div class="clr"></div>
	    	</div>
    	</div>
    </div><div id="bread">
    <a href="social.php">社会招聘</a><span>&nbsp;</span><a href="position.php">职位搜索</a><span>&nbsp;</span>GY0-【国际业务部】Senior Web Developer（Hong Kong）
</div>
<div id="position_detail" class="maxwidth">
    <div class="box wcont_a">
        <div class="blueline">
            <div class="butzwss left"></div>
            <div class="clr"></div>
        </div>
        <form id="searchform" class="buts1" action="position.php">
            <div id="searchrow1">
                <div id="search1"><input id="search2" name="keywords" t="请输入关键词" value="" class="left" style="color: rgb(136, 136, 136);"><input class="left" id="search3" type="submit" value="">
                    <div class="clr"></div>
                </div>
                <input type="hidden" name="lid" value="0">
                <input type="hidden" name="tid" value="0">
            </div>
            <div id="searchrow2">
                <div class="srow2l left"></div>
                <div class="left items pl9 itemnone" id="additems">
                    <a href="position.php?keywords=&amp;tid=0" class="item active"><span><font>全部</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2218"><span><font>深圳</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2156"><span><font>北京</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2175"><span><font>上海</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2196"><span><font>广州</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2268"><span><font>成都</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2459"><span><font>香港</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2426"><span><font>昆明</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=33"><span><font>美国</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;tid=0&amp;lid=2355"><span><font>武汉</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=32"><span><font>韩国</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=59"><span><font>日本</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2252"><span><font>杭州</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=66"><span><font>印度尼西亚</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=60"><span><font>马来西亚</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2283"><span><font>福州</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2314"><span><font>南宁</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=90"><span><font>荷兰</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2226"><span><font>重庆</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2320"><span><font>合肥</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=45"><span><font>泰国</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2225"><span><font>天津</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2436"><span><font>贵阳</font></span></a>
                                        <a class="item itemhide" href="position.php?keywords=&amp;tid=0&amp;lid=2393"><span><font>太原</font></span></a>
                                    </div>
                <div class="left"><a class="more2">更多</a></div>
                <div class="clr"></div>
            </div>
            <div id="searchrow3">
                <div class="srow2l left"></div>
                <div class="left items pl9">
                    <a href="position.php?keywords=&amp;lid=0" class="item active"><span><font>全部</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=87"><span><font>技术类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=82"><span><font>产品/项目类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=83"><span><font>市场类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=81"><span><font>设计类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=84"><span><font>职能类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=85"><span><font>内容编辑类</font></span></a>
                                        <a class="item" href="position.php?keywords=&amp;lid=0&amp;tid=86"><span><font>客户服务类</font></span></a>
                                    </div>
                <div class="clr"></div>
            </div>
        </form>
        <table class="tablelist textl" cellpadding="0" cellspacing="0">
            <tbody><tr class="h">
                <td colspan="3" class="l2 bold size16" id="sharetitle">GY0-【国际业务部】Senior Web Developer（Hong Kong）</td>
            </tr>
            <tr class="c bottomline">
                <td><span class="lightblue l2">工作地点：</span>深圳</td>
                <td><span class="lightblue">职位类别：</span>技术类</td>
                <td><span class="lightblue">招聘人数：</span>1人</td>
            </tr>
            <tr class="c">
                <td colspan="3" class="l2">
                    <div class="lightblue">工作职责：</div>
                    <ul class="squareli"><li>● Work on new coding project, from initial idea concept till final implementation</li><li>● Managing full application stacks from the OS up through custom applications</li><li>● Cooperation with designers and internal departments for project implementation</li><li>● Work hands-on with cloud products to demonstrate and prototype integrations in customer</li><li>environments</li><li>● Ability to mentor other developers and provide technical direction on application architecture</li><li>● Demonstrable ability to rapidly prototype proofs-of-concept and technical demonstrations</li><li>● Provide technical advice and support to major partners</li></ul>
                </td>
            </tr>
            <tr class="c">
                <td colspan="3" class="l2">
                    <div class="lightblue">工作要求：</div>
                    <ul class="squareli"><li>● Degree holder in Computer Science / Engineering or related technical field</li><li>● 5+ years software application development experience</li><li>● 2+ years experience in cloud-based development and system integration</li><li>● Experience with AI, Big Data and web/app development technologies</li><li>(Kubernetes,Docker,Python,Node.js,ReactJS,CSS,HTML)</li><li>● Experience with enterprise networking concepts (VPN,Proxy,DMZ,LB) and cloud infrastructure</li><li>(AWS,GCP,Azure or other) will be a big advantage</li><li>● Experience with gathering and documenting technical requirements and specifications</li><li>● Experience with creating and working with Application Program Interfaces (APIs)</li><li>● Excellent oral</li></ul>
                </td>
            </tr>
            <tr class="c">
                <td colspan="3" class="l2">
                    <button id="apppos" type="button" class="but2 left" onclick="applyPosition(49099);">申请岗位
                    </button>
                    <button type="button" class="but1 left ml9" onclick="applyPosition(49099,true);">
                        收藏岗位
                    </button>
                    <div id="applyshow" class="ajaxshow none"></div>
                    <div class="clr"></div>
                </td>
            </tr>
            <tr class="c">
                <td colspan="3" class="l2">
                    <div class="bshare-custom icon-medium-plus">
                        <div class="bsPromo bsPromo2"></div>
                        <a title="分享到微信" class="bshare-weixin" href="javascript:void(0);"></a>
                        <a title="分享到QQ空间" class="bshare-qzone"></a>
                        <a title="分享到QQ好友" class="bshare-qqim" href="javascript:void(0);"></a>
                        <a title="分享到新浪微博" class="bshare-sinaminiblog" href="javascript:void(0);"></a>
                    </div>
                    <script type="text/javascript" charset="utf-8" src="//static.bshare.cn/b/buttonLite.js#style=-1&amp;uuid=&amp;pophcol=2&amp;lang=zh"></script>
                    <script type="text/javascript" charset="utf-8" src="//static.bshare.cn/b/bshareC0.js"></script>
                </td>
            </tr>
        </tbody></table>
    </div>
</div>
<div id="homeDep"><table id="homeads"><tbody><tr><td align="center"><a href="http://tencent.avature.net/career" target="blank">全球招聘</a></td><td align="center"><a href="http://game.qq.com/hr/" target="blank">互动娱乐事业群招聘</a></td><td align="center"><a href="http://hr.tencent.com/position.php?lid=&amp;tid=&amp;keywords=WXG" target="blank">微信事业群招聘</a></td><td align="center"><a href="http://hr.qq.com/" target="blank">技术工程事业群招聘</a></td></tr></tbody></table></div>	<div id="footer">
		<div>
			<a href="http://www.tencent.com/" target="_blank">关于腾讯</a><span>|</span><a href="http://www.qq.com/contract.shtml" target="_blank">服务条款</a><span>|</span><a href="http://hr.tencent.com/" target="_blank">腾讯招聘</a><span>|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a><span>|</span><a href="http://gongyi.qq.com/" target="_blank">腾讯公益</a><span>|</span><a href="http://service.qq.com/" target="_blank">客服中心</a>
	    </div>
		<p>Copyright © 1998 - 2019 Tencent. All Rights Reserved.</p>
	</div>
	<script type="text/javascript" src="//tajs.qq.com/stats?sId=64934792" charset="UTF-8"></script>

</body></html>

'''

# print(response.content)

soup=BeautifulSoup(html,'lxml')
# print(soup)
content=soup.select('ul>li')
for tr in content:
    print(tr.text.lstrip())
    with open('home.txt','a',encoding='utf-8') as fp:
        fp.write(tr.text.strip())
# print(content)
