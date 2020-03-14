# coding:utf-8
from flask import Flask

@app.route('/jukeboxes/{int:id}')
def getById():
    """获得一个Jukebox"""
    pass

@app.route('/jukeboxes')
def.getAll():
    """获得全部Jukeboxes"""
    pass

@app.route('/jukeboxes')
def create():
    """创建一个Jukebox"""
    pass




if __name == "__main__":
    app.run(debug=true, port=8080)