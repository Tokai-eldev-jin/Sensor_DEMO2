<!doctype html>
<!--
Copyright 2017-2020 JellyWare Inc. All Rights Reserved.
-->
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="BlueJelly">
    <meta name="viewport" content="width=640, maximum-scale=1.0, user-scalable=yes">
    <title>Current Sensor DEMO</title>
    <link href="https://fonts.googleapis.com/css?family=Lato:100,300,400,700,900" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="style.css">
    <script type="text/javascript" src="bluejelly.js"></script>
    <script type="text/javascript" src="./smoothie.js"></script>
  </head>

<body>
<div class="container">
    <div class="title margin">
        <h4><p id="title" style="color:blue;">Current Sensor Plot</p></h4>
    </div>

    <div class="contents margin">
        <button id="startNotifications" class="button" style="background-color:fuchsia;">Start Notify</button>
        <button id="stopNotifications" class="button" style="background-color:fuchsia;">Stop Notify</button>　　　　
		<input id="write_value" type="text" value="100" size="5" onchange="delaySet()">usec　　
        <button id="write" class="button">Send</button>
		<span id="box" style="position:absolute;left:302px;top:90px;color:blue;">delay時間</span>
        <hr>
        <div id="svg">GRAPH AREA</div>
        <hr>
        <span id="data_box0"> </span>
        <span>　</span>
        <span id="data_box1"> </span>
        <span>　</span>
        <span id="data_box2"> </span>
        <span>　</span>
        <span id="data_box3"> </span>
        <span>　</span>
        <span id="data_box4"> </span>
        <span>　</span>
        <span id="data_box5"> </span>
        <span>　</span>
        <span id="data_box6"> </span>
        <span>　</span>

        <!--<div id="device_name"> </div>
        <div id="uuid_name"> </div>
        
        <div id="status"> </div>-->

    </div>
    <!--<div class="footer margin">
                For more information, see <a href="https://jellyware.jp/kurage" target="_blank">jellyware.jp</a> and <a href="https://github.com/electricbaka/bluejelly" target="_blank">GitHub</a> !
    </div>-->
</div>


<script>
//--------------------------------------------------
//Global変数
//--------------------------------------------------
//BlueJellyのインスタンス生成
const ble = new BlueJelly();
const ble2 = new BlueJelly();

//TimeSeriesのインスタンス生成
const ble_data = new TimeSeries();



var array1 = new Array(100);
for(let i=0;i<100;i++){
	array1[i] = new Array(6);
}


var Yokojiku = new Array(0,6,12,18,24,30,36,42,48,54,60);


let startflag1=0;
let cyc1=0;




//-------------------------------------------------
//smoothie.js
//-------------------------------------------------
function createTimeline() {
    const chart = new SmoothieChart({
        millisPerPixel: 20,
        grid: {
            fillStyle: '#ff8319',
            strokeStyle: '#ffffff',
            millisPerLine: 800
        },
        maxValue: 5000,
        minValue: 0
    });
    chart.addTimeSeries(ble_data, {
        strokeStyle: 'rgba(255, 255, 255, 1)',
        fillStyle: 'rgba(255, 255, 255, 0.2)',
        lineWidth: 4
    });
    chart.streamTo(document.getElementById("chart"), 500);
}


//--------------------------------------------------
//ロード時の処理
//--------------------------------------------------
window.onload = function () {
  //UUIDの設定
  ble.setUUID("UUID1","4fafc201-1fb5-459e-8fcc-c5c9c331914b","beb5483e-36e1-4688-b7f5-ea07361b26a8");
  ble2.setUUID("UUID1","4fafc201-1fb5-459e-8fcc-c5c9c331914b","2049779d-88a9-403a-9c59-c7df79e1dd7c");
  //smoothie.js
  //createTimeline();

	main();
}


//--------------------------------------------------
//Scan後の処理
//--------------------------------------------------
ble.onScan = function (deviceName) {
  //document.getElementById('device_name').innerHTML = deviceName;
  document.getElementById('status').innerHTML = "found device!";
}


//--------------------------------------------------
//ConnectGATT後の処理
//--------------------------------------------------
ble.onConnectGATT = function (uuid) {
  console.log('> connected GATT!');

  //document.getElementById('uuid_name').innerHTML = uuid;
  //document.getElementById('status').innerHTML = "connected GATT!";
}


//--------------------------------------------------
//Read後の処理：得られたデータの表示など行う
//--------------------------------------------------
ble.onRead = function (data, uuid){
	let i;
	let value = "";
	let data1;


	var data_display = new Array('data_box0','data_box1','data_box2','data_box3','data_box4','data_box5','data_box6');
	
	
	//フォーマットに従って値を取得
	for(i=0;i< data.byteLength;i++){
		value = value + String.fromCharCode(data.getInt8(i));
	}
	console.log(value);
	
	//数値化
	let array_atai =value.split(',');
	cyc1=Number(array_atai[0]);

	if(cyc1<3){
		for(i=1;i<=100;i++){
			data1=Number(array_atai[i])/4095;
			data1=data1*3300;
			data1=Math.round(data1);
			array1[i-1][cyc1] = Number(data1);
		}
	}else{
		for(i=1;i<=100;i++){
			data1=Number(array_atai[i])/4095;
			data1=data1*4095;
			data1=Math.round(data1);
			array1[i-1][cyc1] = Number(data1);
		}
	}

	if(cyc1==5){
		startflag1 = 1;
	}
	

	//document.getElementById('uuid_name').innerHTML = uuid;
	//document.getElementById('status').innerHTML = "read data"
	
	//グラフへ反映
	//ble_data.append(new Date().getTime(), value);

}


//--------------------------------------------------
//Write後の処理
//--------------------------------------------------
ble2.onWrite = function(uuid){
  //document.getElementById('uuid_name').innerHTML = uuid;
  //document.getElementById('status').innerHTML = "written data"
}




//--------------------------------------------------
//Start Notify後の処理
//--------------------------------------------------
ble.onStartNotify = function(uuid){
  console.log('> Start Notify!');

  //document.getElementById('uuid_name').innerHTML = uuid;
  //document.getElementById('status').innerHTML = "started Notify";
}


//--------------------------------------------------
//Stop Notify後の処理
//--------------------------------------------------
ble.onStopNotify = function(uuid){
  console.log('> Stop Notify!');

  //document.getElementById('uuid_name').innerHTML = uuid;
  //document.getElementById('status').innerHTML = "stopped Notify";
}


//-------------------------------------------------
//ボタンが押された時のイベント登録
//--------------------------------------------------
document.getElementById('startNotifications').addEventListener('click', function() {
      ble.startNotify('UUID1');
});

document.getElementById('stopNotifications').addEventListener('click', function() {
      ble.stopNotify('UUID1');
});


document.getElementById('write').addEventListener('click', function() {
  //フォーマットに従って値を変換
  const textEncoder = new TextEncoder();
  const text_data = String(document.getElementById('write_value').value);
  const text_data_encoded = textEncoder.encode(text_data + '\n');

  //write
  console.log(text_data);
  ble2.write('UUID1', text_data_encoded);

	let i;
	let time_intarval;
	time_intarval = Number(text_data)*100/1000;//ms
	time_intarval += 50;
	time_intarval /= 10;
	
	for(i=0;i<=10;i++){
		Yokojiku[i]=data1=Math.round(time_intarval*i);
	}
	

});



const wait = (ms) => {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, ms);
  });
};


async function main() {
	while(true){
	    await wait(100); //
	    Create_grapf();
	}
}


function delaySet() {
	const textEncoder = new TextEncoder();
	const text_data = String(document.getElementById('write_value').value);
	const text_data_encoded = textEncoder.encode(text_data + '\n');

	  //write
	  console.log(text_data);
	  ble2.write('UUID1', text_data_encoded);

	let i;
	let time_intarval;
	time_intarval = Number(text_data)*100/1000;//ms
	time_intarval += 50;
	time_intarval /= 10;

	for(i=0;i<=10;i++){
		Yokojiku[i]=data1=Math.round(time_intarval*i);
	}
}









function Create_grapf(Sensor_val) {
	let screen_w = 650;
	let screen_h = 400;
	let Max_val = 5000;
	let Min_val = 0;
	let x1;
	let x2;
	let y1;
	let y2;
	
	let i=0;
	let ii=0;
	var plot_color = new Array('red','tomato','deeppink','blue','mediumblue','darkblue','pink','teal','lime','aqua','yellow','maroon','gray','silver','skyblue');
	/*var Yokojiku = new Array('0.0','0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0');*/
	var label =  new Array('Core1','Core2','Core3','shunt1','shunt2','shunt3');
	
	if(startflag1==1){
		let display_text="<svg xmlns='http://www.w3.org/2000/svg' version='1.1' height='" + screen_h + "' width='" + screen_w + "' viewBox='-100 -10 900 520' class='SvgFrame'>";
		
		/*display_text = display_text + "<line x1='0' y1='0' x2='" + screen_w + "' y2='0' style='stroke:black;stroke-width:1' />";
		display_text = display_text + "<line x1='0' y1='" + screen_h + "' x2='" + screen_w + "' y2='" + screen_h + "' style='stroke:black;stroke-width:1' />";
		display_text = display_text + "<line x1='0' y1='0' x2='0' y2='" + screen_h + "' style='stroke:black;stroke-width:1' />";
		display_text = display_text + "<line x1='" + screen_w + "' y1='0' x2='" + screen_w + "' y2='" + screen_h + "' style='stroke:black;stroke-width:1' />";
		*/
		
		//外枠
		display_text = display_text + "<rect x='0' y1='0' width='"+screen_w+"' height='"+screen_h+"' fill='white'  style='stroke:gray;stroke-width:1' />"
		
		//横目盛り線
		for(i=1;i<=9;i++){
			display_text = display_text + "<line x1='0' y1='" + screen_h/10*i + "' x2='" +  screen_w + "' y2='" + screen_h/10*i + "' style='stroke:gray;stroke-width:1' />";
		}

		//縦目盛り線
		for(i=1;i<=10;i++){
			display_text = display_text + "<line x1='" + screen_w/10*i + "' y1='0' x2='" + (screen_w/10*i) + "' y2='" + screen_h + "' style='stroke:gray;stroke-width:1' />";
		}

		//横目盛り
		for(i=0;i<=10;i++){	
			display_text = display_text + "<text fill='#448aff' font-family='Script' font-weight='bold'  x='" + screen_w/10*i + "' y='"+(screen_h+30)+"' font-size='20' text-anchor='middle' stroke-width='1'>"+Yokojiku[i]+"</text>"
		}
		
		//縦目盛り
		for(i=0;i<=10;i++){
	        display_text = display_text + "<text  fill='#448aff' font-family='Script' font-weight='bold'  x='-5' y='"+ (screen_h/10*i+10) +"' font-size='20' text-anchor='end' stroke-width='1'>"+(Max_val-(Max_val-Min_val)/10*i)+"</text>"
	    }
	    
		
		//##########　X軸のタイトル表示　##########
		display_text = display_text + "<text  fill='#448aff' fill='#448aff' font-family='Comic Sans MS' font-weight='bold'  x='"+screen_w/10*5+"' y='"+(screen_h+70)+"' font-size='25' text-anchor='middle' stroke-width='1'>時間（msec）</text>"
		

		//##########　Y軸のタイトル表示　##########
		display_text = display_text + "<text  fill='#448aff' font-family='Script' font-weight='bold'  x='"+(-1*screen_h/2)+"' y='-75' font-size='25' text-anchor='middle' stroke-width='1' transform='rotate(-90,0,0)'>Voltage(mV)</text>"
		
		
		for(ii=0;ii<6;ii++){
		    x1 = 0;
		    
		    for(i=0;i<=98;i++){
		    	x2=0;
		        x2 = x1 + screen_w/100;
		        y1 = array1[i][ii]
		        y1 -= Min_val;
		        y1 *= screen_h;
		        y1 /= (Max_val - Min_val);
		        if(y1<0) y1=0;
		        if(y1>screen_h) y1=screen_h;
		        
		        y1 = screen_h - y1;
		        
		        y2 =  array1[(i+1)][ii];
		        y2 -= Min_val;
		        y2 *= screen_h;
		        y2 /= (Max_val - Min_val);
		        if(y2<0) y2=0;
		        if(y2>screen_h) y2=screen_h;
		        
		        y2 = screen_h - y2;
		        display_text = display_text + "<line x1='" + x1 + "' y1='" + y1 + "' x2='" + x2 + "' y2='" + y2 + "' style='stroke:"+ plot_color[ii] +";stroke-width:2' />";
		        
		        x1 += screen_w / 100
		        
		    }
	    }


		/*ラベル作成*/
		display_text = display_text + "<rect x='"+(screen_w/10*10.1)+"' y='"+(screen_h/10-10)+"' width='140' height='130' fill='floralwhite'  style='stroke:gray;stroke-width:1' />"
		for(i=0;i<6;i++){
			display_text = display_text + "<line x1='"+(screen_w/10*10.2)+"' y1='"+(screen_h/10+i*20)+"' x2='" +(screen_w/10*10.2+20)+ "' y2='" + (screen_h/10+i*20)+ "' style='stroke:"+plot_color[i]+";stroke-width:2' />";
			display_text = display_text + "<text  fill='"+plot_color[i]+"' font-family='Script' font-weight='bold' x='"+(screen_w/10*10.2+25)+"' y='"+(screen_h/10+i*20+10)+"' font-size='20' text-anchor='start' stroke-width='1'>"+label[i]+"</text>";
		}


	    
	    display_text += "</svg>"
	    document.getElementById("svg").innerHTML =  display_text;

		startflag1=0;
	}


}

</script>
</body>
</html>
