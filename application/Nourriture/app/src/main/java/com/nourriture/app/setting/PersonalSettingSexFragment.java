package com.nourriture.app.setting;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/14.
 */
public class PersonalSettingSexFragment extends Fragment implements View.OnClickListener {
    private View view;
    private String sex;
    boolean isTwoPane;

    @Override
    public void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);

        //get sex and isTwoPane from Bundle--tablet or Intent--phone
        if (getArguments()!=null && getArguments().containsKey("sex") && getArguments().containsKey("isTwoPane")) {
            sex = getArguments().getString("sex");
            isTwoPane = getArguments().getBoolean("isTwoPane");
        } else if (getActivity().getIntent().getStringExtra("sex") != null) {
            sex = getActivity().getIntent().getStringExtra("sex");
            isTwoPane = getActivity().getIntent().getBooleanExtra("isTwoPane", false);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.setting_sex_frag, container, false);

        flag(sex);

        view.findViewById(R.id.sex_male).setOnClickListener(this);
        view.findViewById(R.id.sex_female).setOnClickListener(this);

        return view;
    }

    @Override
    public void onClick(View view){
        TextView text = (TextView) view;
        String new_sex = text.getText().toString().toLowerCase();

        if (isTwoPane) {
            // refresh the value of sex in the left fragment
            PersonalSettingFragment personalSettingFragment = (PersonalSettingFragment)
                    getActivity().getSupportFragmentManager().getFragments().get(0); //maybe there is a better way to get the fragmant
            personalSettingFragment.changeValue(3, new_sex);
        } else {
            // return the value of sex to PersonalSettingFragment
            Intent intent = getActivity().getIntent();
            intent.putExtra("sex", new_sex);
            getActivity().setResult(3, intent);
            getActivity().finish();
        }

        flag(new_sex);
        sex = new_sex;
    }

    // put a flag on the row
    private void flag(String sex){
        TextView male = (TextView) view.findViewById(R.id.sex_male);
        TextView female = (TextView) view.findViewById(R.id.sex_female);
        Drawable select = this.getResources().getDrawable(R.drawable.check_mark);

        if (sex.equals("male")) {
            male.setCompoundDrawablesWithIntrinsicBounds(null, null, select, null);
            female.setCompoundDrawablesWithIntrinsicBounds(null, null, null, null);
        } else if (sex.equals("female")) {
            male.setCompoundDrawablesWithIntrinsicBounds(null, null, null, null);
            female.setCompoundDrawablesWithIntrinsicBounds(null, null, select, null);
        }
    }
}
