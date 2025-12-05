# tests/test_simple_storage.py
import brownie
from brownie import SimpleStorage, accounts

def test_deploy():
    """测试合约部署"""
    # 部署合约
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    
    # 验证初始值
    assert simple_storage.getValue() == 100

def test_set_value():
    """测试设置值"""
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    
    # 设置新值
    tx = simple_storage.setValue(42, {"from": accounts[0]})
    
    # 验证值已更新
    assert simple_storage.getValue() == 42
    
    # 验证事件触发
    assert "ValueChanged" in tx.events
    assert tx.events["ValueChanged"]["newValue"] == 42

def test_increment():
    """测试递增函数"""
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    
    # 先设置值
    simple_storage.setValue(10, {"from": accounts[0]})
    
    # 递增
    simple_storage.increment({"from": accounts[0]})
    
    # 验证结果
    assert simple_storage.getValue() == 11

def test_only_owner_can_set():
    """测试权限控制"""
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    
    # 使用不同账户尝试设置值
    with brownie.reverts():
        simple_storage.setValue(100, {"from": accounts[1]})
      # 如果合约允许任何人设置值，测试应该通过
    # simple_storage.setValue(42, {"from": accounts[1]})
    # assert simple_storage.getValue() == 42