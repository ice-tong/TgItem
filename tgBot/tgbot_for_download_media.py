# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 03:55:19 2018

@author: icetong
"""

import telebot
import requests, os

token = "" #此处填入你的tg机器人apitoken
store = './data'

bot = telebot.TeleBot(token, num_threads=64)

def download(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)

@bot.message_handler(content_types="photo")
def get_photoes(message:telebot.types.Message):
    #print(message)
    message_dict = message.json
    chat_type = message_dict['chat']['type']
    if chat_type == 'private':
        chat_title = message_dict['chat']['username']
    else:
        chat_title = message_dict['chat']['title']
    photo = message_dict['photo'][-1]
    photo_file_id = photo['file_id']
    photo_file_info = bot.get_file(photo_file_id)
    photo_file_path = photo_file_info.file_path
    photo_url = 'https://api.telegram.org/file/bot{}/{}'.format(token, photo_file_path)
    print('从聊天对话：', chat_title, '嗅探到图片：', photo_file_path, '开始下载。。')
    
    file_dir = store + '/' + chat_title.replace('/', '').replace(',', '') + '/photo'
    photo_name = '{}_{}'.format(photo_file_id, photo_file_path.split('/')[-1])
    photo_path = file_dir + '/' + photo_name
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    download(photo_url, photo_path)
    print('下载完成：', photo_file_path)
    
@bot.message_handler(content_types="video")
def get_videos(message:telebot.types.Message):
    #print(message)
    video = message.video
    chat_type = message.chat.type
    if chat_type == 'private':
        chat_title = message.chat.username
    else:
        chat_title = message.chat.title
    video_file_id = video.file_id
    video_file_path = bot.get_file(video_file_id).file_path
    video_url = 'https://api.telegram.org/file/bot{}/{}'.format(token, video_file_path)
    print('从聊天对话：', chat_title, '嗅探到视频：', video_file_path, '开始下载。。')
    
    file_dir = store + '/' + chat_title.replace('/', '').replace(',', '') + '/video'
    video_name = '{}_{}'.format(video_file_id, video_file_path.split('/')[-1])
    video_path = file_dir + '/' + video_name
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    download(video_url, video_path)
    print('下载完成：', video_file_path)
    
bot.polling()
