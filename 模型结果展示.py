# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 23:11:03 2024

@author: wooji
"""

import streamlit as st
import numpy as np
from joblib import load

# 加载保存的模型
model = load('random_forest_model_.joblib')

# 特征列表
features = ['物理工艺', '化学工艺', '生物工艺', '物理化学工艺', '生物化学工艺', '废水实际处理能力']

# Streamlit应用的主函数
def run():
    st.title('东莞电镀行业废水处理单位治理成本预测')

    # 创建单选按钮
    feature_selections = {
        feature: st.radio(feature, ['有', '无'])
        for feature in features[:-1]  # 除了废水实际处理能力之外的所有特征
    }

    # 废水实际处理能力的数值输入
    wastewater_treatment_capacity = st.number_input('废水实际处理能力（吨/天）', min_value=0, step=1)

    # 确认按钮
    result = st.button("确认")

    # 根据用户选择和输入构建特征数组
    if result:
        feature_values = [
            1 if feature_selections[feature] == '有' else 0
            for feature in features[:-1]  # 将前五个特征转换为数值
        ]
        feature_values.append(wastewater_treatment_capacity)  # 添加废水处理能力数值

        # 将特征列表转换为numpy数组
        features_array = np.array(feature_values).reshape(1, -1)

        # 使用模型进行预测
        prediction = model.predict(features_array)
        result = round(prediction[0],2)
        # 显示预测结果
        st.write(f'预测单位废水治理成本: {result}'+'元/吨')

if __name__ == "__main__":

    run()
