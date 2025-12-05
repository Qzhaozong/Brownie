#### Brownie 框架安装
python3 --version
pip3 --version
git --version

#### 在当前用户安装brownie，加上镜像源
pip3 install --user eth-brownie --index-url https://mirrors.aliyun.com/pypi/simple/
#### 验证安装
brownie --version

#### 创建项目目录
mkdir my-brownie-project
cd my-brownie-project

#### 初始化 Brownie 项目
brownie init

#### 项目结构会自动创建：
my-brownie-project/
├── contracts/
├── interfaces/
├── scripts/
├── tests/
├── brownie-config.yaml
└── README.md

my-brownie-project/
├── contracts/           # Solidity 合约
├── interfaces/          # 接口定义
├── scripts/             # 部署和交互脚本
├── tests/               # 测试文件
│   ├── conftest.py      # 测试配置
│   └── test_xxx.py      # 测试文件
├── reports/             # 测试报告（自动生成）
├── build/               # 编译输出（自动生成）
├── brownie-config.yaml  # 配置文件
└── README.md


#### 创建 .env 文件，添加下方文件
#### Infura 或 Alchemy
export WEB3_INFURA_PROJECT_ID=your_infura_project_id
export WEB3_ALCHEMY_PROJECT_ID=your_alchemy_api_key
#### 钱包私钥（用于部署）
export PRIVATE_KEY=your_wallet_private_key
#### Etherscan API（用于验证）
export ETHERSCAN_TOKEN=your_etherscan_api_key
#### 加载环境变量
source .env
#### 2. 配置 Brownie
cd 项目目标地址
brownie networks delete development 2>/dev/null || true
brownie networks add development development \
    cmd=ganache \
    host=http://127.0.0.1 \
    port=8545 \
    accounts=10
#### 安装 Ganache（本地测试网络）
npm install  ganache。
#### 创建符号链接到全局位置
sudo ln -sf "$(pwd)/node_modules/.bin/ganache" /usr/local/bin/ganache
#### 验证
which ganache
ganache --version
#### 查找 ganache 的位置
which ganache
#### 创建符号链接
sudo ln -sf $(which ganache) /usr/local/bin/ganache-cli
#### 验证
ganache-cli --version
#### 启动 Ganache
ganache --port 8545 --chain.chainId 1337