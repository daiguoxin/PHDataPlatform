    function get_help(page_name){
        layer.open({
            type: 2 //此处以iframe举例
            ,title: '帮助中心-'+page_name
            ,area: ['430px', '100%']
            ,shadeClose: false
            ,maxmin: true
            ,offset: 'r'
            ,scrollbar: true
            ,content: '/help_center/page/'
            ,zIndex: layer.zIndex //重点1
          });
    }

