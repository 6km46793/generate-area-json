# 简介
根据配置文件来生成部分省份地区的 json 文件。

## 配置文件
config.json：用户端配置文件，该文件已加入到 ignore，所以用户修改本文件，不会影响代码。一般是用户首次运行时创建本问价，并将 defaultConfig.json 文件的数据拷贝过来，然后根据每次打包的需求修改配置文件。

defaultConfig.json：如果用户没有config.json 文件，那么程序将读本文件的配置。

### 配置解释
目前只有四个字段，具体解释如下：

merge：主要是针对直辖市，如北京。有些时候，不需要区分市辖区和县，有的时候需要区分。如果该字段为 true，生成的 json 文件将不区分市辖区和县；如果为 false 那么生成的 json 文件将区分市辖区和县。（注：区分和不区分的情况下，具体县的 code 将不一样）。

outputFileName：生成 json 文件的名字，程序运行完成后，将过滤出的结果保存到外部 json 文件中，该字段就是生成的文件名，并存放在 ./output 目录下，该目录下的 json 文件已加入到 ignore。

key：在过滤省份的时候，可以根据省份的名字（key 为 des），也可以根据省份的 code （key 为 code）来过滤。如果改项配置没有，程序默认取 des 为过滤条件。

provinceList：要过滤出的省份列表。

## 其他注意事项
1 完整的数据是 ./src/allArea_merge.json 和 ./src/allArea_separate.json。
2 ./src/provinceList.json 文件 有完整的省份名字列表和省份 code 列表，在新建任务的时候，可以考虑从此处拷贝一份，然后根据自己的需求删减。
3 nodejs 运行方法： node index.js
