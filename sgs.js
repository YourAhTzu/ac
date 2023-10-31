const axios = require('axios');

const tokens = process.env.sgs.split('@');

function sign(token) {
    const url = 'https://fwdt.shengongshe.org/sgsWchartApi/api/My/sign';
    const headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Token': token,
    };

    axios.get(url, { headers })
        .then((response) => {
            const data = response.data;
            const msg = data.msg;
            console.log('签到结果:', msg);
        })
        .catch((error) => {
            console.error('签到失败:', error.message);
        });
}

function getMediaIds(token) {
    const url = 'https://fwdt.shengongshe.org/sgsWchartApi/api/ImageText/list';
    const headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Token': token,
    };
    const params = {
        page: 1,
    };

    axios.post(url, null, { headers, params })
        .then((response) => {
            const data = response.data.data;
            const newsList = data.news;
            const mediaIds = newsList.map(news => news.media_id);
            mediaIds.sort(() => 0.5 - Math.random()); // Shuffle the mediaIds
            return mediaIds.slice(0, 3);
        })
        .then((mediaIds) => {
            console.log('随机获取的媒体ID列表:', mediaIds);
            console.log('开始执行阅读任务');
            for (const mediaId of mediaIds) {
                executeUrl(token, mediaId);
            }
        })
        .catch((error) => {
            console.error('获取媒体ID失败:', error.message);
        });
}

function executeUrl(token, mediaId) {
    const url = 'https://fwdt.shengongshe.org/sgsWchartApi/api/ImageText/read';
    const headers = {
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Origin': 'https://fwdt.shengongshe.org',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2f) NetType/WIFI Language/zh_CN',
        'Token': token,
    };
    const data = {
        media_id: mediaId,
    };

    axios.post(url, data, { headers })
        .then((response) => {
            const msg = response.data.msg;
            console.log(`运行结果：${msg}`);
        })
        .catch((error) => {
            console.error('执行URL失败:', error.message);
        });
}

console.log('开始签到');
for (const token of tokens) {
    sign(token);
    getMediaIds(token);
    console.log('====================================');
}