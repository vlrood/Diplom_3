script_drag_and_drop = """var t=arguments,e=t[0],n=t[1],i=t[2]||0,o=t[3]||0,r=t[4]||1,
        a=t[5]||'',s='alt'===a||'\ue00a'===a,l='ctrl'===a||'\ue009'===a,
        c='shift'===a||'\ue008'===a,u=e.ownerDocument,
        f=e.getBoundingClientRect(),g=n?n.getBoundingClientRect():f,
        p=f.left+f.width/2,d=f.top+f.height/2,h=g.left+(i||g.width/2),
        m=g.top+(o||g.height/2),v=u.elementFromPoint(p,d),
        y=u.elementFromPoint(h,m);if(!v||!y){
        var E=new Error('source or target element is not interactable');
        throw E.code=15,E}var _={constructor:DataTransfer,effectAllowed:null,
        dropEffect:null,types:[],files:Object.setPrototypeOf([],null),
        _items:Object.setPrototypeOf([],{add:function(t,e){
        this[this.length]={_data:''+t,kind:'string',
        type:e,getAsFile:function(){},getAsString:function(t){t(this._data)}},
        _.types.push(e)},remove:function(t){
        Array.prototype.splice.call(this,65535&t,1),_.types.splice(65535&t,1)},
        clear:function(t,e){this.length=0,_.types.length=0}}),
        setData:function(t,e){this.clearData(t),this._items.add(e,t)},
        getData:function(t){for(var e=this._items.length;
        e--&&this._items[e].type!==t;);return e>=0?this._items[e]._data:null},
        clearData:function(t){for(var e=this._items.length;
        e--&&this._items[e].type!==t;);this._items.remove(e)},
        setDragImage:function(t){}};function w(t,e,n,i){
        for(var o=0;o<e.length;++o){var r=u.createEvent('MouseEvent');
        r.initMouseEvent(e[o],!0,!0,u.defaultView,0,0,0,p,d,l,s,c,!1,0,null),
        t.dispatchEvent(r)}i&&setTimeout(i,n)}function D(t,e,n,i){
        var o=u.createEvent('DragEvent');o.initMouseEvent(
        e,!0,!0,u.defaultView,0,0,0,p,d,l,s,c,!1,0,null),Object.setPrototypeOf(
        o,null),o.dataTransfer=_,Object.setPrototypeOf(o,DragEvent.prototype),
        t.dispatchEvent(o),i&&setTimeout(i,n)}
        'items'in DataTransfer.prototype&&(_.items=_._items),
        w(v,['pointerdown','mousedown'],1,function(){
        for(var t=v;t&&!t.draggable;)t=t.parentElement;if(t&&t.contains(v)){
        var e=y.getBoundingClientRect();D(v,'dragstart',r,function(){
        var t=y.getBoundingClientRect();p=t.left+h-e.left,d=t.top+m-e.top,D(
        y,'dragenter',1,function(){D(y,'dragover',r,
        function(){D(u.elementFromPoint(p,d),'drop',1,function(){D(v,'dragend',
        1,function(){w(u.elementFromPoint(p,d),
        ['mouseup','pointerup'])})})})})})}})"""