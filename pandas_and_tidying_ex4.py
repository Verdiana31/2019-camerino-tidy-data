new=pd.merge(mutations.reset_index(drop=True),
                       sampleruns.reset_index(drop=True),
                       left_on=['Strain ID','Population','Generation'],
                       right_on=['Strain ID','Population','Generation'],
                       how='right',
                      )
