
layui.define(['element'], function(exports) {
    var $ = layui.jquery
    ,element = layui.element
    ,layer = layui.layer
    ,device = layui.device();

    //阻止IE7以下访问
    if(device.ie && device.ie < 8){
        layer.alert('Layui最低支持ie8，您当前使用的是古老的 IE'+ device.ie + '，你丫的肯定不是程序猿！');
    }
    var treeMobile = $('.site-tree-mobile'),
    shadeMobile = $('.site-mobile-shade');

    treeMobile.on('click', function() {
        $('body').addClass('site-mobile');
    });
    shadeMobile.on('click', function() {
        $('body').removeClass('site-mobile');
    });
    exports('global', {});
});