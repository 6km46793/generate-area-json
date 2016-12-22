var _ = require('underscore'),
    fs = require('fs');

var config = {};
try {
    config = require('./config');
} catch(error) {
    try {
        config = require('./defaultConfig');
    } catch(error) {
        console.log('配置文件读取失败，请确定 ./config.json 或者 ./defaultConfig.json 是否存在');
        return;
    }
}
var provinceList = config.merge ? require('./allArea_marge') : require('./allArea_separate');

var result = [];
var key = config.key ? config.key : 'des';

_.each(config.provinceList, function(item) {
    var temp = _.find(provinceList, function(province) {
        return item == province[key];
    });
    if (temp) {
        result.push(temp);
    }
});

fs.writeFile('output/' + config.outputFileName + '.json', JSON.stringify(result), function(err) {
    if (err) {
        console.log(err);
        return;
    } else {
        console.log('save success');
    }
});
