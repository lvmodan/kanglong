## kanglong

https://www.joinquant.com/research
#### 降龙四式之亢龙有悔

> 这一招叫作‘亢龙有悔’，掌法的精要不在‘亢’字而在‘悔”字。倘若只求刚猛狠辣，亢奋凌厉，只要有几百斤蛮力，谁都会使了。这招又怎能教黄药师佩服？‘亢龙有悔，盈不可久’，因此有发必须有收。打出去的力道有十分，留在自身的力道却还有二十分。哪一天你领会到了这‘悔’的味道，这一招就算是学会了三成。好比陈年美酒，上口不辣，后劲却是醇厚无比，那便在于这个‘悔’字。” --洪帮主

这是一个根据PE、PB在指数历史低估区间时买入，长期持有，然后在PE、PB处于历史高位时卖出的策略。

* 这个策略极其简单，适用于大部分宽基指数；
* 这个策略是跑不赢指数的，但是能让你极其安心的长期持有；

* 谨记：一切回测有效的策略都是看后视镜开车。回测仅仅是参考，不能预测未来。
* 谨记：成功概率不能预测，失败风险无法回避，历史周期不断重复，时刻抱有敬畏之心。

#### 指数特点

* 背靠国运，不死鸟
* 长期上涨
* 成本低
* 不择股
* 容易量化
* 大道至简

## 低估不定期不定额策略

我们的策略制定原则：

1. 可复现、可回测
2. 排除人工干扰，机器拯救人类
3. 落子无悔，买定离手
4. 低估买，高估卖，没有机会不动
5. 资金分为250份分批投入

### 买入条件

1. 市场出现系统性低估机会可以买入
2. 单一标的PE、PB 处于历史30%以下可以买入
4. PB处于历史30%以下，且PE<10 或 1/PE<十年期国债利率X2，可以买入
5. 对于消费指数、医药指数、养老指数等PB从未小于2的品种，我们只在PB,PE均在历史10%的区间内才买入一份，也就是百里挑一；

### 卖出条件

1. 市场出现系统性高估机会可以卖出
2. 单一标的PE、PB 处于历史70%以上可以卖出
5. 1/PE<市场能找到的最小无风险收益率，可以卖出置换

### 简单持有

不符合买入，也不符合卖出条件，简单持有即可。

若市场利率缓慢下行，可简单买入短债基金持有，其他情况不动。

### 凯利公式控制每次买入份额

采用[银行螺丝钉](https://xueqiu.com/3079173340/62032246)的方法计算仓位；

其盈利增长率我们替换为10年ROE中位值，因为长远来看，PEG会趋近于ROE；用ROE更加保险

以恒生指数为例。

* 恒生指数过去10年的ROE中位值10%左右
* 我们期望5年年化15%的收益率
* PE历史30%大概为12，配合我们上面要求的条件，我们需要在10PE买入

#### 凯利公式

```
F =（bp - q）/ b
```

其中b代表赔率，p代表获胜率，q代表落败率，q = 1-p

#### 投资指数基金的赔率

```
赔率b =（卖出时估值/买入时估值）*【1+指数盈利增长率】^持有年数 =（1+你要求的年复合收益率）^持有年数

b = （卖出时估值/买入时估值）* 1.1^5 = 1.15^5

卖出时估值PE/10 ≈ 1.25

要求卖出时估值 ≈ 12.5

```

这样就把我们的投资行为固化为了这样一个事件：

假如未来恒生指数能保持平均10%的ROE，我们在10PE买入恒生指数，要求有15%的年复合收益率，那我们“需要在5年的时间里，至少有一次机会在12.5倍以上市盈率卖出”。


#### 投资指数基金的胜率

```
胜率 = 期望卖出PE的历史估值概率
```

5年时间里，12.5PE是大概率事件，事实上，我们要求在70%的PE上方卖出，这个值大概是15PE。

12.5PE在历史上大概处于 60%的位置， 所以我们的条件还是非常宽松的。

按照我们前面制定的的边界卖出条件 PE估值百分位 > 70%，所以如果能买到10PE以下的恒生指数，并且期望5年内年化收益15%的话，只要能持有不动，胜率>60%；

#### 计算仓位

通过凯利公式计算出来的仓位， X0.5；称为半凯利公式

胜率60%，赔率2；

```
F =（bp-q）/b = (2 * 60% - 40%)/2 = 40%

F * 0.5 = 20%
```
根据半凯利公式推出，推荐仓位为20%。

激进的投资者可以选择凯利公式原始值，即40%；

#### 一些推论

* 预期收益越低，胜率就会越高，仓位也会越高。如果预期收益过高，甚至仓位会是负数（也就是无法实现）
* 买入估值越低，胜率就会越高，仓位也会越高。如果买入估值过高，甚至仓位会是负数（无法赚取估值差收益）
* 指数的盈利增长率越高，对应的胜率也会越高
* 买入时不要求每次都能赢，但是一定要在赢面大的时候下大注

#### 多指数组合计算仓位

对组合中的每个指数设定 买入PE，卖出PE，持有年数，要求年复合增长率， 分别计算仓位

全部仓位相加，便可以决定总仓位。

#### 定投

每次的总仓位即 定投总额 / 定投次数；比如5年计划投入60w，每月定投一次，那么每次总仓位1w；

每次计算卖出PE点大于历史估值70%即可盈利的品种，并决定仓位；然后所有仓位相加。

如果定投不定额， 每次仓位可以超过100%；

如果定投定额，每个品种的仓位比例再等分平均，最后达到100%

如果没有符合条件的品种或者总仓位<100%，买入短债基金代替；

达到卖出条件分批减仓，减仓可以逆运算，也可以简单的用一个网格策略逐步卖出。

#### 不定期不定额

如果我们有一个量化策略，可以直接把投入资金分为50份，在某个品种达到极高的胜率的时候计算仓位一把买入；然后在此之上， 采用价值平均策略定投，长期持有；


#### FAQ

* 实盘在哪里？

https://www.joinquant.com/algorithm/live/liveUrlShareIndex?backtestId=9ce88469ba4da2c4ad0be340e0509a8e

密码:jiosim

且慢实盘同步 (且慢的收益率是默认将流动资金按照货基收益来计算的，所以会跟聚宽有一定差别，按实际情况来说，且慢计算的更准):

https://qieman.com/portfolios/ZH035242

* 为什么资金分成250份？

综合考虑Beta因子、费率、波动率、夏普比例等等因素，选择5只宽基指数，每只预计投入资金50份；50X5=250；

如果有更多的资金，能选取关联度小的更多的宽基指数，当然可以分成更多份；

* 250不吉利啊

投资永远都有赌运的成分，just for fun.

* 为什么每只指数预计50份？

A股牛短熊长，一个熊市周期在5-7年内，每周执行一次，5-7年里大概产生产生50次买入的机会

* 为什么卖出策略这么简单，不能采用凯利公式减仓吗？

牛短熊长，切勿贪心。

当已买入的品种处于>70%的历史区间时，我们每次都会卖出5份，也就是总持有份额的2% (1/250 X 5), 这是根据A股市场的牛熊持续周期比例确定的；

* 低估的条件是否太苛刻了。连2018年那种情况都没满仓？

把这个策略看成是一个人的话，他超级胆小，超级吝啬，超级怕死，只有在他的把握非常非常大的时候，才敢抛出仅仅一个筹码。即使是2018年的钻石底，他买入也很少。

这个策略基本上建仓时间在3年以上，什么也不做的时间基本上5年以上。这段时间内，现金可以买入货基打底。所以这个策略的收益你可以再乐观的 3%+；

我相信一个策略带有其人格化，我相信世界上有许多极度胆小，不求暴富，只希望四平八稳取得微小的幸福的人，理所当然应该有这个极度简单，极度保守的策略来服务他们；

* 为什么不在绝对历史低估的时候一把梭？

一个极度保守，极度胆小，超级吝啬，超级怕死的人，这辈子会一把梭吗？ 我认为这么一个人这辈子任何情况下都不会一把梭，即使天上掉馅饼，他也会躲着走怕砸到头。

* 为什么要设定PB<2的坎？

像消费、医药、养老等指数，PB历史区间从未<2；所以我们设定了一个`更宽松`的条件，即PB、PE均处于最近5年10%低估范围内，才买入一份；

* 我们是对消费、医药、养老指数有偏见吗？

当然，在我们的估值体系里面，任何PB>2的企业估值都是不可接受的；我们也清楚这是一个看起来很`荒谬`的偏见；但是我们做一个思想实验：

> 在一个自由流通，没有限制的贸易世界中，存在某个企业或某种行业，能一直维持远远超出自身净资产的高估值吗？

答案是没有这样的企业，如果这个世界是自由竞争的，即使出现了生产长生不老药的公司，长期来看也一定会出现其挑战者拉低其估值。

* 可是，这个世界不是想象中的世界啊？这个世界有垄断、贪婪等等，一定会有某个行业或企业维持其高估值几十年的。

是的，但是我们作为一个极度胆小的人，对这样的企业会赞叹敬佩，却永远不会去赌他`发明了长生不老药`。
